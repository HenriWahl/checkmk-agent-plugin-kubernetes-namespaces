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
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic

# default interval in seconds
DEFAULT_INTERVAL = 60.0


def _migrate_int_to_float(value: object) -> Mapping[str, object]:
    """
    migrate from integer interval to float interval for backward compatibility
    """
    if value is not None and isinstance(value, dict):
        # convert integer interval to float if present
        if 'interval' in value and isinstance(value['interval'], int):
            return {
                'interval': float(value['interval']),
                'kubeconfig_path': value.get('kubeconfig_path', '')
            }
    return value


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
    )


rule_spec_kubernetes_namespaces_bakery = AgentConfig(
    title=Title('Kubernetes Namespaces'),
    name='kubernetes_namespaces',
    parameter_form=_parameter_form_kubernetes_namespaces_bakery,
    topic=Topic.APPLICATIONS,
    help_text=Help('This will deploy the agent plugin <tt>kubernetes_namespaces</tt> '
                   'for monitoring Kubernetes namespace resources.'),
)
