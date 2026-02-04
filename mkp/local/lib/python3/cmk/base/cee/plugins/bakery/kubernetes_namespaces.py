# Server-side bakery part of plugin for monitoring Kubernetes namespaces
# Bakery definition at lib/python3/cmk/base/cee/plugins/bakery/kubernetes_namespaces.py
# inspired by https://exchange.checkmk.com/p/hello-bakery and
# https://github.com/mschlenker/checkmk-snippets/tree/main/mkp/hellobakery
# ©2024 henri.wahl@ukdd.de

from pathlib import Path
from typing import Any

from cmk.base.cee.plugins.bakery.bakery_api.v1 import FileGenerator, OS, Plugin, PluginConfig, register


def get_kubernetes_namespaces_files(conf: Any) -> FileGenerator:
    """
    Simple bakery plugin generator for kubernetes_namespaces

    conf is a dictionary like: {'deploy': {'interval': 60.0, 'kubeconfig_path': '/etc/kubernetes/admin.conf'}}
    For backward compatibility, it may also be a flat dictionary like: {'interval': 60.0, 'kubeconfig_path': '/etc/kubernetes/admin.conf'}
    """

    # debugging
    # with open('/tmp/debug.txt', 'a') as debug_file:
    #     debug_file.write(f'config: {conf}\n')

    # Extract interval and kubeconfig_path from nested 'deploy' structure
    interval = None
    kubeconfig_path = None

    if isinstance(conf, dict):
        # Handle new nested structure
        if conf.get('deploy') is not None and isinstance(conf['deploy'], dict):
            deploy_conf = conf['deploy']
            if deploy_conf.get('interval') is not None:
                interval = int(deploy_conf['interval'])
            if deploy_conf.get('kubeconfig_path'):
                kubeconfig_path = deploy_conf.get('kubeconfig_path')
        # Handle old flat structure for backward compatibility
        else:
            if conf.get('interval') is not None:
                interval = int(conf['interval'])
            if conf.get('kubeconfig_path'):
                kubeconfig_path = conf.get('kubeconfig_path')

    # only makes sense on Linux so just create for that OS
    yield Plugin(base_os=OS.LINUX,
                 source=Path('kubernetes_namespaces'),
                 interval=interval
                 )

    # add config file if kubeconfig_path is set
    if kubeconfig_path:
        yield PluginConfig(base_os=OS.LINUX,
                           lines=[f"KUBECONFIG={kubeconfig_path}"],
                           target=Path("kubernetes_namespaces.cfg"),
                           include_header=True)


# register the bakery plugin with its arguments
register.bakery_plugin(
    name='kubernetes_namespaces',
    files_function=get_kubernetes_namespaces_files
)
