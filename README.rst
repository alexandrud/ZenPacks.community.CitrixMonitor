=============================================================================
ZenPacks.community.CitrixMonitor
=============================================================================


About
=============================================================================
This project is a Zenoss_ extension (ZenPack) that allows for monitoring of
Citrix XEN Servers via commands sent over ssh. The plugin is derived from 
`ZenPack.zenoss.XenMonitor` and depends on `ZenPack.zenoss.ZenossVirtualHostMonitor`::

The 

.. _ZenPack.zenoss.XenMonitor: http://community.zenoss.org/docs/DOC-5803
      .. _ZenPack.zenoss.ZenossVirtualHostMonitor: http://community.zenoss.org/docs/DOC-5802


Features
-----------------------------------------------------------------------------

The plugin adds a new device class named Citrix under Server > Virtual Machine Host
and creates a list of guests for each monitored server.

Prerequisites
-----------------------------------------------------------------------------

==================  =========================================================
Prerequisite        Restriction
==================  =========================================================
ZenOSS              4.2 or higher
ZenPacks            ZenPack.zenoss.Zenoss.ZenossVirtualHostMonitor 2.4.0 or
                    higher
Monitored machines  SSH keyed access to the monitored machines on a user
                    that has access to run ``xe vm-list params`` command
==================  =========================================================


Installation
-------------------------------------------------------------------------------

This ZenPack has no special installation considerations.

Configuration
-------------------------------------------------------------------------------

Installing the ZenPack will add the following items to your Zenoss system.

* Device Classes

  * /Server/Virtual Machine Host/Citrix

* Modeler Plugins

  * community.cmd.Citrix

Usage
-----------------------------------------------------------------------------

Add an Citrix Server
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Navigate to the `Infrastructure` page

2. Go to `Devices>Server>Virtual Host Machine>Citrix`

3. Click on the `Add a single device / Add multiple devices`

4. Wait for the device to be modeled.

5. Navigate to the new device.

   .. note:: 

        In the XenMonitor plugin documentation there was a note to add the
        device directly into the right container. Although I haven't tested
        it I think that applies here too.


Change Log
-----------------------------------------------------------------------------

1.0.0 - 2012-10-12
~~~~~~~~~~~~~~~~~

* First release
