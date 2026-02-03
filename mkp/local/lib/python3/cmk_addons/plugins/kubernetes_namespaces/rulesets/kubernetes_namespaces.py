#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
"""Discovery rules for Kubernetes Namespaces"""

from cmk.rulesets.v1 import Help, Title
from cmk.rulesets.v1.form_specs import (
    BooleanChoice,
    DefaultValue,
    DictElement,
    Dictionary,
    List,
    String,
)
from cmk.rulesets.v1.rule_specs import DiscoveryParameters, Topic


def _parameter_form_kubernetes_namespaces_discovery():
    return Dictionary(
        title=Title("Kubernetes Namespaces Discovery"),
        help_text=Help("Configure which Kubernetes resources should be discovered per namespace"),
        elements={
            "kubernetes_namespaces": DictElement(
                parameter_form=List(
                    title=Title("Namespace-specific discovery settings"),
                    help_text=Help("Configure resource discovery for specific namespaces"),
                    element_template=Dictionary(
                        title=Title("Namespace settings"),
                        elements={
                            "namespace": DictElement(
                                parameter_form=String(
                                    title=Title("Namespace"),
                                    help_text=Help(
                                        "Apply only to this namespace - if not used, the resources settings apply to all namespaces"
                                    ),
                                ),
                                required=False,
                            ),
                            "cronjobs": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("Cronjobs"),
                                    label=Title("Discover CronJobs"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                            "daemonsets": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("DaemonSets"),
                                    label=Title("Discover DaemonSets"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                            "deployments": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("Deployments"),
                                    label=Title("Discover Deployments"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                            "persistent_volumes": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("PersistentVolumes"),
                                    label=Title("Discover PersistentVolumes"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                            "pods": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("Pods"),
                                    label=Title("Discover Pods"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                            "replicasets": DictElement(
                                parameter_form=BooleanChoice(
                                    title=Title("ReplicaSets"),
                                    label=Title("Discover ReplicaSets"),
                                    prefill=DefaultValue(True),
                                ),
                                required=False,
                            ),
                        },
                    ),
                ),
                required=False,
            ),
        },
    )


rule_spec_kubernetes_namespaces_discovery = DiscoveryParameters(
    name="kubernetes_namespaces",
    title=Title("Kubernetes Namespaces Discovery"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_form_kubernetes_namespaces_discovery,
)

