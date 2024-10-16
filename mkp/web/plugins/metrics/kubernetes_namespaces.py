# Server-side metrics settings for plugin for monitoring Kubernetes namespaces,
# resides at share/web/plugins/metrics/kubernetes_namespaces.py
# ©2024 henri.wahl@ukdd.de

# just in case:
# _cmk_color_palette = {
#     # do not use:
#     #   '0'     : (0.33, 1, 1),  # green
#     #   '1'     : (0.167, 1, 1), # yellow
#     #   '2'     : (0, 1, 1),     # red
#     # red area
#     '11': (0.775, 1, 1),
#     '12': (0.8, 1, 1),
#     '13': (0.83, 1, 1),
#     '14': (0.05, 1, 1),
#     '15': (0.08, 1, 1),
#     '16': (0.105, 1, 1),
#     # yellow area
#     '21': (0.13, 1, 1),
#     '22': (0.14, 1, 1),
#     '23': (0.155, 1, 1),
#     '24': (0.185, 1, 1),
#     '25': (0.21, 1, 1),
#     '26': (0.25, 1, 1),
#     # green area
#     '31': (0.45, 1, 1),
#     '32': (0.5, 1, 1),
#     '33': (0.515, 1, 1),
#     '34': (0.53, 1, 1),
#     '35': (0.55, 1, 1),
#     '36': (0.57, 1, 1),
#     # blue area
#     '41': (0.59, 1, 1),
#     '42': (0.62, 1, 1),
#     '43': (0.66, 1, 1),
#     '44': (0.71, 1, 1),
#     '45': (0.73, 1, 1),
#     '46': (0.75, 1, 1),
#     # special colors
#     '51': (0, 0, 0.5),  # grey_50
#     '52': (0.067, 0.7, 0.5),  # brown 1
#     '53': (0.083, 0.8, 0.55),  # brown 2
# }


from cmk.gui.i18n import _
from cmk.gui.plugins.metrics import graph_info, metric_info

# --- PersistentVolumes ---

metric_info['persistent_volume_used'] = {
    'title': _('Persistent Volume Used'),
    'unit': 'bytes',
    'color': '15/a',
}

metric_info['persistent_volume_capacity'] = {
    'title': _('Persistent Volume Capacity'),
    'unit': 'bytes',
    'color': '35/a',
}

metric_info['persistent_volume_percentage'] = {
    'title': _('Persistent Volume Percentage'),
    'unit': '%',
    'color': '45/a',
}

graph_info['persistent_volumes_combined'] = {
    'title': _('Persistent Volumes'),
    'metrics': [
        ('persistent_volume_used', 'line'),
        ('persistent_volume_capacity', 'line')
    ],
}

# --- Pods ---

metric_info['pods_running'] = {
    'title': _('Pods Running'),
    'unit': 'count',
    'color': '36/a',
}

metric_info['pods_waiting'] = {
    'title': _('Pods Waiting'),
    'unit': 'count',
    'color': '33/a',
}

metric_info['pods_terminated'] = {
    'title': _('Pods Terminated'),
    'unit': 'count',
    'color': '34/a',
}

metric_info['pods_crashing'] = {
    'title': _('Pods Crashing'),
    'unit': 'count',
    'color': '12/a',
}

graph_info['pods_combined'] = {
    'title': _('Pods'),
    'metrics': [
        ('pods_running', 'line'),
        ('pods_waiting', 'line'),
        ('pods_terminated', 'line'),
        ('pods_crashing', 'line')
    ],
}

# --- Deployments ---

metric_info['deployments_replicas'] = {
    'title': _('Deployments Replicas'),
    'unit': 'count',
    'color': '32/a',
}

metric_info['deployments_ready_replicas'] = {
    'title': _('Deployments Ready Replicas'),
    'unit': 'count',
    'color': '23/a',
}

metric_info['deployments_unavailable_replicas'] = {
    'title': _('Deployments Unavailable Replicas'),
    'unit': 'count',
    'color': '15/a',
}

graph_info['deployments_combined'] = {
    'title': _('Deployments'),
    'metrics': [
        ('deployments_replicas', 'line'),
        ('deployments_ready_replicas', 'line'),
        ('deployments_unavailable_replicas', 'line')
    ],
}

# --- DaemonSets ---

metric_info['daemonsets_current_number_scheduled'] = {
    'title': _('DaemonSets Current Number Scheduled'),
    'unit': 'count',
    'color': '31/a',
}

metric_info['daemonsets_desired_number_scheduled'] = {
    'title': _('DaemonSets Desired Number Scheduled'),
    'unit': 'count',
    'color': '32/a',
}

metric_info['daemonsets_number_ready'] = {
    'title': _('DaemonSets Number Ready'),
    'unit': 'count',
    'color': '33/a',
}

metric_info['daemonsets_number_unavailable'] = {
    'title': _('DaemonSets Number Unavailable'),
    'unit': 'count',
    'color': '12/a',
}

graph_info['daemonsets_combined'] = {
    'title': _('DaemonSets'),
    'metrics': [
        ('daemonsets_current_number_scheduled', 'line'),
        ('daemonsets_desired_number_scheduled', 'line'),
        ('daemonsets_number_ready', 'line'),
        ('daemonsets_number_unavailable', 'line')
    ],
}

# --- CronJobs ---

metric_info['cronjobs_active'] = {
    'title': _('CronJobs active'),
    'unit': 'count',
    'color': '31/a',
}

# --- ReplicaSets ---

metric_info['replicasets_replicas'] = {
    'title': _('Replicasets Replicas'),
    'unit': 'count',
    'color': '31/a',
}

metric_info['replicasets_ready_replicas'] = {
    'title': _('Replicasets Ready Replicas'),
    'unit': 'count',
    'color': '32/a',
}

metric_info['replicasets_unavailable_replicas'] = {
    'title': _('Replicasets Unavailable Replicas'),
    'unit': 'count',
    'color': '33/a',
}

graph_info['replicasets_combined'] = {
    'title': _('Replica Sets'),
    'metrics': [
        ('replicasets_replicas', 'line'),
        ('replicasets_ready_replicas', 'line'),
        ('replicasets_unavailable_replicas', 'line')
    ],
}