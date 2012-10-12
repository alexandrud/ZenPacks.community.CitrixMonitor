##############################################################################
# 
# Copyright (C) Zenoss, Inc. 2009, all rights reserved.
# 
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
# 
##############################################################################


__doc__="""Citrix XenServer
Plugin to gather information about virtual machines running
under Xen
"""
import re
import Globals
from Products.DataCollector.plugins.CollectorPlugin \
     import CommandPlugin
from Products.DataCollector.plugins.DataMaps \
     import ObjectMap

class Citrix(CommandPlugin):
    """
    Fetch data from a Citrix server using ssh and the xe command
    """
    relname = "guestDevices"
    modname = 'ZenPacks.zenoss.ZenossVirtualHostMonitor.VirtualMachine'
	# The next command lists all parameters available from the xe command for all guest
    command = '/opt/xensource/bin/xe vm-list is-control-domain=false params'

    def copyDataToProxy(self, device, proxy):
        result = CommandPlugin.copyDataToProxy(self, device, proxy)
        proxy.guestDevices = [g.id for g in device.guestDevices()]
        return result
    
    def process(self, device, results, log):
        log.info('Collecting interfaces for device %s' % device.id)
        log.debug('Results from %s = "%s"', self.command, results)

        rm = self.relMap()
        before = set(device.guestDevices)
        vmRegex = re.compile(r'\n\n\n')
        vmDataRegex = re.compile(r'\s*uuid.*:\s*(?P<uuid>.*?)$.*'
            r'name-label.*?:\s*(?P<name>.*?)$.*'
            r'power-state.*?:\s*(?P<state>.*?)$.*'
            r'memory-actual.*?:\s*(?P<memory>\d+)$.*'
            r'VCPUs-number.*?:\s*(?P<cpus>\d+)$.*'
            r'os-version.*?:\s*(name:\s*)?(?P<os>.*?)((;.*?)|(\|.*?))?$.*'
            , re.M | re.S | re.I)
        #for guestData in results.re.compile(\n\n\n).split[1:]:
        for guestData in re.split(r'\n\n\n', results):
            result = vmDataRegex.search(guestData)
            if result:
                name = result.group('name')
                uuid = result.group('uuid')
                cpus = result.group('cpus')
                memory = int(result.group('memory')) / 1024.0 / 1024.0
                state = result.group('state')
                os = result.group('os')
            else:
                log.warn("Ignoring %s as data missing (eg ID, Mem,"
                    " VCPUs, State info): ",
                    name)
                continue
            info = {}
            if state == 'running':
                info['adminStatus'] = True
                info['operStatus'] = True
            if state == 'halted':
                info['adminStatus'] = False
                info['operStatus'] = True
            if state == 'paused':
                info['adminStatus'] = False
                info['operStatus'] = True
            if state == 'suspended':
                info['adminStatus'] = False
                info['operStatus'] = True
            if state == 'unknown':
                info['adminStatus'] = False
                info['operStatus'] = False
            if state == 'unrecognized':
                info['adminStatus'] = False
                info['operStatus'] = False
            info['memory'] = int(memory)
            if re.search(r'(<not in database>|PV-drivers-version.*)', os):
                info['osType'] = 'N/A - Not from Template'
            else:
                info['osType'] = os
            info['displayName'] = name
            om = self.objectMap(info)
            om.id = self.prepId(name)
            before.discard(om.id)
            rm.append(om)

        for id in before:
            om = self.objectMap(dict(adminStatus=False))
            om.id = id
            rm.append(om)

        return [rm]
