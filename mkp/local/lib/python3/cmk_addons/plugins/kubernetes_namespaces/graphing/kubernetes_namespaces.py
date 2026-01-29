#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# Server-side metrics settings for plugin for monitoring Kubernetes namespaces
# ©2024 henri.wahl@ukdd.de

from cmk.graphing.v1 import Title, Color, graphs, metrics

# --- PersistentVolumes ---

metric_persistent_volume_used = metrics.Metric(
    name='persistent_volume_used',
    title=Title('Persistent Volume Used'),
    unit=metrics.Unit(metrics.DecimalNotation("B")),
    color=Color.DARK_RED,
)

metric_persistent_volume_capacity = metrics.Metric(
    name='persistent_volume_capacity',
    title=Title('Persistent Volume Capacity'),
    unit=metrics.Unit(metrics.DecimalNotation("B")),
    color=Color.DARK_GREEN,
)

metric_persistent_volume_percentage = metrics.Metric(
    name='persistent_volume_percentage',
    title=Title('Persistent Volume Percentage'),
    unit=metrics.Unit(metrics.DecimalNotation("%")),
    color=Color.DARK_BLUE,
)

graph_persistent_volumes = graphs.Graph(
    name='persistent_volumes_combined',
    title=Title('Persistent Volumes'),
    simple_lines=[
        'persistent_volume_used',
        'persistent_volume_capacity'
    ],
)

# --- Pods ---

metric_pods_running = metrics.Metric(
    name='pods_running',
    title=Title('Pods Running'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.GREEN,
)

metric_pods_waiting = metrics.Metric(
    name='pods_waiting',
    title=Title('Pods Waiting'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.YELLOW,
)

metric_pods_terminated = metrics.Metric(
    name='pods_terminated',
    title=Title('Pods Terminated'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.GRAY,
)

metric_pods_crashing = metrics.Metric(
    name='pods_crashing',
    title=Title('Pods Crashing'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.RED,
)

graph_pods = graphs.Graph(
    name='pods_combined',
    title=Title('Pods'),
    simple_lines=[
        'pods_running',
        'pods_waiting',
        'pods_terminated',
        'pods_crashing'
    ],
)

# --- Deployments ---

metric_deployments_replicas = metrics.Metric(
    name='deployments_replicas',
    title=Title('Deployments Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.DARK_GREEN,
)

metric_deployments_ready_replicas = metrics.Metric(
    name='deployments_ready_replicas',
    title=Title('Deployments Ready Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.GREEN,
)

metric_deployments_unavailable_replicas = metrics.Metric(
    name='deployments_unavailable_replicas',
    title=Title('Deployments Unavailable Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.RED,
)

graph_deployments = graphs.Graph(
    name='deployments_combined',
    title=Title('Deployments'),
    simple_lines=[
        'deployments_replicas',
        'deployments_ready_replicas',
        'deployments_unavailable_replicas'
    ],
)

# --- DaemonSets ---

metric_daemonsets_current_number_scheduled = metrics.Metric(
    name='daemonsets_current_number_scheduled',
    title=Title('DaemonSets Current Number Scheduled'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.DARK_GREEN,
)

metric_daemonsets_desired_number_scheduled = metrics.Metric(
    name='daemonsets_desired_number_scheduled',
    title=Title('DaemonSets Desired Number Scheduled'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.GREEN,
)

metric_daemonsets_number_ready = metrics.Metric(
    name='daemonsets_number_ready',
    title=Title('DaemonSets Number Ready'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.LIGHT_GREEN,
)

metric_daemonsets_number_unavailable = metrics.Metric(
    name='daemonsets_number_unavailable',
    title=Title('DaemonSets Number Unavailable'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.RED,
)

graph_daemonsets = graphs.Graph(
    name='daemonsets_combined',
    title=Title('DaemonSets'),
    simple_lines=[
        'daemonsets_current_number_scheduled',
        'daemonsets_desired_number_scheduled',
        'daemonsets_number_ready',
        'daemonsets_number_unavailable'
    ],
)

# --- CronJobs ---

metric_cronjobs_active = metrics.Metric(
    name='cronjobs_active',
    title=Title('CronJobs Active'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.DARK_GREEN,
)

# --- ReplicaSets ---

metric_replicasets_replicas = metrics.Metric(
    name='replicasets_replicas',
    title=Title('ReplicaSets Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.DARK_GREEN,
)

metric_replicasets_ready_replicas = metrics.Metric(
    name='replicasets_ready_replicas',
    title=Title('ReplicaSets Ready Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.GREEN,
)

metric_replicasets_unavailable_replicas = metrics.Metric(
    name='replicasets_unavailable_replicas',
    title=Title('ReplicaSets Unavailable Replicas'),
    unit=metrics.Unit(metrics.DecimalNotation("")),
    color=Color.RED,
)

graph_replicasets = graphs.Graph(
    name='replicasets_combined',
    title=Title('Replica Sets'),
    simple_lines=[
        'replicasets_replicas',
        'replicasets_ready_replicas',
        'replicasets_unavailable_replicas'
    ],
)
