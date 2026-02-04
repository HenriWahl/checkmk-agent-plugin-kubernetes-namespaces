#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
from collections.abc import Mapping

from cmk.rulesets.v1 import (
    Help,
    Label,
    Title,
)

from cmk.rulesets.v1.form_specs import (
    DictElement,
    Dictionary,
    DefaultValue,
    TimeSpan,
    TimeMagnitude,
    String
)
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic, Title, Help

# default interval in seconds
DEFAULT_INTERVAL = 60.0


def _migrate_int_to_float(value: object) -> Mapping[str, object]:
    """
    migrate from integer interval to float interval for backward compatibility
    and migrate from old flat structure to new nested 'deploy' structure
    """
    if value is not None and isinstance(value, dict):
        # if already in new format with 'deploy' key
        if 'deploy' in value:
            deploy_val = value['deploy']
            if isinstance(deploy_val, dict):
                # convert integer interval to float if present
                if 'interval' in deploy_val and isinstance(deploy_val['interval'], int):
                    result = {
                        'deploy': {
                            'interval': float(deploy_val['interval'])
                        }
                    }
                    if 'kubeconfig_path' in deploy_val:
                        result['deploy']['kubeconfig_path'] = deploy_val['kubeconfig_path']
                    return result
            return value
        # backward compatibility - migrate from old flat structure to new nested structure
        elif 'interval' in value or 'kubeconfig_path' in value:
            result = {'deploy': {}}
            if 'interval' in value:
                interval_val = value['interval']
                result['deploy']['interval'] = float(interval_val) if isinstance(interval_val, int) else interval_val
            if 'kubeconfig_path' in value:
                result['deploy']['kubeconfig_path'] = value['kubeconfig_path']
            return result
    # empty dictionary means no deployment
    return value if value else dict()


def _parameter_form_kubernetes_namespaces_bakery() -> Dictionary:
    """
    definition of the parameter form for the Kubernetes namespaces bakery plugin
    :return:
    """
    return Dictionary(
        migrate=_migrate_int_to_float,
        title=Title('Kubernetes Namespaces'),
        help_text=Help('This will deploy the agent plugin <tt>kubernetes_namespaces</tt>. This will activate the '
                       'check <tt>kubernetes_namespaces</tt> on Kubernetes hosts and monitor namespace resources.'
                       ),
        elements={
            'deploy': DictElement(
                parameter_form=Dictionary(
                    title=Title('Deploy plugin'),
                    help_text=Help(
                        'Configure how the <tt>kubernetes_namespaces</tt> plugin will run on a deployed agent. '
                        'Leave this section empty to disable the plugin on the deployed agent.'),
                    elements={
                        'interval': DictElement(
                            parameter_form=TimeSpan(
                                title=Title('Run asynchronously'),
                                label=Label('Interval for collecting data'),
                                help_text=Help(
                                    'Determines how often the plugin will run on a deployed agent.'),
                                displayed_magnitudes=[TimeMagnitude.SECOND,
                                                      TimeMagnitude.MINUTE,
                                                      TimeMagnitude.HOUR,
                                                      TimeMagnitude.DAY],
                                prefill=DefaultValue(DEFAULT_INTERVAL),
                            ),
                            required=False,
                        ),
                        'kubeconfig_path': DictElement(
                            parameter_form=String(
                                title=Title('Path for Kubernetes configuration file'),
                                label=Label('Full path like /etc/kubernetes/admin.conf'),
                                help_text=Help(
                                    'Set the KUBECONFIG environment variable for the plugin. Leave empty to use the default kubeconfig location.'),
                            ),
                            required=False,
                        )
                    },
                ),
            )
        },
    )


rule_spec_kubernetes_namespaces_bakery = AgentConfig(
    title=Title('Kubernetes Namespaces'),
    name='kubernetes_namespaces',
    parameter_form=_parameter_form_kubernetes_namespaces_bakery,
    topic=Topic.APPLICATIONS,
    help_text=Help('This will deploy the agent plugin <tt>kubernetes_namespaces</tt> '
                   'for monitoring Kubernetes namespace resources.'),
)
