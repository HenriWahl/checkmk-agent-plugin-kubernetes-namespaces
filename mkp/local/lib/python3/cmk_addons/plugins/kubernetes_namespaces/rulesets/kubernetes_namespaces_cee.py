# Server-side WATO settings for bakery for plugin for monitoring Kubernetes namespaces,
# resides at share/check_mk/web/plugins/wato/kubernetes_namespaces_bakery.py
# ©2024 henri.wahl@ukdd.de

from cmk.gui.i18n import _
from cmk.gui.plugins.wato import (
    HostRulespec,
    rulespec_registry,
)
from cmk.gui.valuespec import (
    Age,
    Dictionary,
    TextAscii,
)

# Flag to check if the bakery WATO settings should be used
USE_BAKERY_WATO = True

try:
    # Import the necessary module for Checkmk CEE
    from cmk.gui.cee.plugins.wato.agent_bakery.rulespecs.utils import RulespecGroupMonitoringAgentsAgentPlugins
except ModuleNotFoundError:
    # If the module is not found, it is not a Checkmk CEE instance
    print("This is not a Checkmk CEE instance and so kubernetes_namespaces bakery WATO can't be loaded.")
    USE_BAKERY_WATO = False


def _valuespec_kubernetes_namespaces():
    """
    Define the GUI specification for Kubernetes namespaces.

    :return: Dictionary object containing the GUI specification.
    """
    return Dictionary(
        title=_('Kubernetes namespaces'),
        help=_('Deploys the agent plugin for Kubernetes namespaces'),
        elements=[
            # Define the interval for collecting data asynchronously
            ('interval',
             Age(
                 title=_('Run asynchronously'),
                 label=_('Interval for collecting data'),
                 default_value=60,  # default: 1 minute
             )
             ),
            ('kubeconfig_path',
             TextAscii(
                 title=_('Path for Kubernetes configuration file in environment variable KUBECONFIG'),
                 label=_('Full path like /etc/kubernetes/admin.conf'),
                 default_value='',
                 size=50
             )
             ),
        ],
        # keys named here get an option checkbox in the WATO UI
        optional_keys=['interval', 'kubeconfig_path'],
    )


if USE_BAKERY_WATO:
    # Register the rulespec for Kubernetes namespaces in the agent bakery
    # Only if the Checkmk CEE module is available aka it is a CEE instance
    rulespec_registry.register(
        HostRulespec(
            group=RulespecGroupMonitoringAgentsAgentPlugins,
            name='agent_config:kubernetes_namespaces',
            valuespec=_valuespec_kubernetes_namespaces,
        ))
