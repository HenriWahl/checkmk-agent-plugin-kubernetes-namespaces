#!/usr/bin/env python3
"""Checkmk 2.4 rule specification for Kubernetes Namespaces Check Parameters"""

from cmk.rulesets.v1 import Title
from cmk.rulesets.v1.form_specs import (
    DefaultValue,
    DictElement,
    Dictionary,
    Integer,
    LevelDirection,
    Percentage,
    SimpleLevels,
)
from cmk.rulesets.v1.rule_specs import CheckParameters, Topic, HostAndItemCondition


def _parameter_form_kubernetes_namespaces():
    return Dictionary(
        title=Title("Kubernetes Namespaces Check Parameters"),
        elements={
            "percentage_persistent_volumes": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Percentage threshold for persistent volumes"),
                    form_spec_template=Percentage(),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=DefaultValue(value=(80.0, 90.0)),
                ),
                required=False,
            ),
            "threshold_cronjob_count": DictElement(
                parameter_form=SimpleLevels(
                    title=Title("Threshold for CronJob count"),
                    form_spec_template=Integer(unit_symbol="count"),
                    level_direction=LevelDirection.UPPER,
                    prefill_fixed_levels=DefaultValue(value=(2, 3)),
                ),
                required=False,
            ),
        }
    )


rule_spec_kubernetes_namespaces = CheckParameters(
    name="kubernetes_namespaces",
    title=Title("Kubernetes Namespaces Check Parameters"),
    topic=Topic.APPLICATIONS,
    parameter_form=_parameter_form_kubernetes_namespaces,
    condition=HostAndItemCondition(item_title=Title("Kubernetes namespace resource")),
)
