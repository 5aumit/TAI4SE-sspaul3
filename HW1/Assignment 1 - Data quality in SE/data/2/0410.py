#
# -*- coding: utf-8 -*-
# Copyright 2019 Fortinet, Inc.
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
"""
The fortios firewall monitor class
It is in this file the runtime information is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""
from __future__ import absolute_import, division, print_function
__metaclass__ = type

import re
from copy import deepcopy

from ansible.module_utils.network.common import utils
from ansible.module_utils.network.fortios.argspec.firewall.firewall import FirewallArgs


FACT_SYSTEM_SUBSETS = frozenset([
    'system_current-admins_select',
    'system_firmware_select',
    'system_fortimanager_status',
    'system_ha-checksums_select',
    'system_interface_select',
    'system_status_select',
    'system_time_select',
])


class FirewallFacts(object):
    """ The fortios firewall fact class
    """

    def __init__(self, module, fos, uri=None, subspec='config', options='options'):
        self._module = module
        self._fos = fos
        self._uri = uri

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for firewall
        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf
        :rtype: dictionary
        :returns: facts
        """
        fos = self._fos if self._fos else connection
        vdom = self._module.params['vdom']
        ansible_facts['ansible_network_resources'].pop('system', None)
        facts = {}
        if self._uri.startswith(tuple(FACT_SYSTEM_SUBSETS)):
            resp = fos.monitor('system', self._uri[len('system_'):].replace('_', '/'), vdom=vdom)
            facts.update({self._uri: resp})
        ansible_facts['ansible_network_resources'].update(facts)
        return ansible_facts

