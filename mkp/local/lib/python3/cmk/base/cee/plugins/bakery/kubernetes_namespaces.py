#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

from pathlib import Path
from typing import Any

from cmk.base.cee.plugins.bakery.bakery_api.v1 import FileGenerator, OS, Plugin, PluginConfig, register


def get_kubernetes_namespaces_files(conf: Any) -> FileGenerator:
    """
    Simple bakery plugin generator for kubernetes_namespaces

    conf looks like: {'deployment': ('deploy', {'interval': 60.0, 'kubeconfig_path': '/etc/kubernetes/admin.conf'})}
    mind the tuple!
    """

    # debugging
    # with open('/tmp/debug.txt', 'a') as debug_file:
    #     debug_file.write(f'config: {conf}\n')

    if isinstance(conf, dict):
        # default to no interval - will be filled if set in config
        interval = None
        kubeconfig_path = None

        # new config structure since version 2.4
        if conf.get('deployment'):
            if isinstance(conf['deployment'], tuple) and conf['deployment'][0] == 'deploy':
                # this is a tuple ('deploy', { ... })
                deploy = conf['deployment'][1]
                if isinstance(deploy, dict) and \
                        deploy.get('interval'):
                    interval = int(deploy['interval'])
                if isinstance(deploy, dict) and \
                        deploy.get('kubeconfig_path'):
                    kubeconfig_path = deploy.get('kubeconfig_path')
            elif isinstance(conf['deployment'], tuple) and conf['deployment'][0] == 'no_deploy':
                return

        # backward compatibility - check older config options
        else:
            if conf.get('interval') is not None:
                interval = conf.get('interval')
            if conf.get('kubeconfig_path') is not None:
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
