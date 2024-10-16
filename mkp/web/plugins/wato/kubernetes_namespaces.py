# Server-side WATO settings for plugin for monitoring Kubernetes namespaces,
# resides at share/check_mk/web/plugins/wato/kubernetes_namespaces.py
# ©2024 henri.wahl@ukdd.de

from cmk.gui.i18n import _

from cmk.gui.valuespec import (
    Dictionary,
    Integer,
    Percentage,
    TextInput,
    Tuple,
)

from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithItem,
    rulespec_registry,
    RulespecGroupCheckParametersApplications,
)


def _item_kubernetes_namespaces():
    """
    Define the item specification for Kubernetes namespaces.

    :return: TextInput object for Kubernetes namespaces.
    """
    return TextInput(
        title='Kubernetes Namespaces',
        help='Settings for Kubernetes namespaces',
    )


def _parameter_kubernetes_namespaces():
    """
    Define the parameter specification for Kubernetes namespaces in Web GUI.

    :return: Dictionary object containing parameter specifications.
    """
    return Dictionary(
        elements=[
            # Define the percentage thresholds for persistent volumes
            ('percentage_persistent_volumes',
             Tuple(
                 title=_("Percentage threshold for persistent volumes "),
                 elements=[
                     Percentage(title=_('Warning'), default_value=80.0),
                     Percentage(title=_('Critical'), default_value=90.0),
                 ]
             )
             ),
            # Define the threshold for CronJob count
            ('threshold_cronjob_count',
             Tuple(
                 title=_("Threshold for CronJob count"),
                 elements=[
                     Integer(title=_('Warning'), default_value=2, unit='count'),
                     Integer(title=_('Critical'), default_value=3, unit='count'),
                 ]
             )
             )
        ]
    )


# Register the rulespec for Kubernetes namespaces
rulespec_registry.register(
    CheckParameterRulespecWithItem(
        check_group_name='kubernetes_namespaces',
        group=RulespecGroupCheckParametersApplications,
        match_type='dict',
        item_spec=_item_kubernetes_namespaces,
        parameter_valuespec=_parameter_kubernetes_namespaces,
        title=lambda: _('Kubernetes Namespaces'),
    )
)