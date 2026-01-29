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
    CascadingSingleChoice,
    CascadingSingleChoiceElement,
    FixedValue,
    TimeSpan,
    TimeMagnitude,
    String
)
from cmk.rulesets.v1.rule_specs import AgentConfig, Topic

# default interval in seconds
DEFAULT_INTERVAL = 60.0


def _migrate_int_to_float(value: object) -> Mapping[str, object]:
    """
    migrate from integer interval to float interval
    """
    if value is not None:
        # backward compatibility - migrate from deploy to deployment
        if value.get('interval'):
            return {
                'deployment': {
                    'deploy': {
                        'interval': float(value['interval']),
                        'kubeconfig_path': value.get('kubeconfig_path', '')
                    }
                }
            }
        # backward compatibility
        elif value.get('kubeconfig_path'):
            return {
                'deployment': {
                    'deploy': {
                        'interval': DEFAULT_INTERVAL,
                        'kubeconfig_path': value.get('kubeconfig_path')
                    }
                }
            }
        else:
            return value
    else:
        return {
            'deployment': {
                'no_deploy': True
            }
        }


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
            'deployment': DictElement(
                required=True,
                parameter_form=CascadingSingleChoice(
                    title=Title('Deployment options'),
                    prefill=DefaultValue('deploy'),
                    help_text=Help(
                        'Determines how the <tt>kubernetes_namespaces</tt> plugin will run on a deployed agent or disables it on a deployed agent'),
                    elements=[
                        CascadingSingleChoiceElement(
                            name='deploy',
                            title=Title("Deploy the Kubernetes Namespaces Check"),
                            parameter_form=Dictionary(
                                title=Title('Kubernetes Namespaces Check'),
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
                                        )
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
                                }
                            ),
                        ),
                        CascadingSingleChoiceElement(
                            name='no_deploy',
                            title=Title("Do not deploy the Kubernetes Namespaces Check"),
                            parameter_form=FixedValue(value=True),
                        )
                    ]
                ),
            ),
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
