=============================================================================
ZenPacks.community.CitrixMonitor
=============================================================================


About
=============================================================================
This project is a Zenoss extension (ZenPack) that allows for monitoring of
Citrix XEN Servers via commands sent over ssh. The plugin is derived from 
`XenMonitor zenpack <http://community.zenoss.org/docs/DOC-5803>`_ and depends on `ZenossVirtualHostMonitor zenpack <http://community.zenoss.org/docs/DOC-5802>`_ ::

.. _XenMonitor zenpack: http://community.zenoss.org/docs/DOC-5803/
.. _ZenossVirtualHostMonitor zenpack: http://community.zenoss.org/docs/DOC-5802/



Disclaimer
-----------------------------------------------------------------------------

This is an "it worked on my machine" zenpack and, if you use it, you use it at
your own peril. If you can try it in a development environment first I 
strongly advise it.


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

There isn't any ``.egg`` file yet. To install it you will need to use the 
developer installation method. Do the following as the zenoss user:

    .. code:: bash

        cd /your/working/directory/of/choice
        git clone git://github.com/alexandrud/ZenPacks.community.CitrixMonitor.git
        zenpack --link --install ZenPacks.community.CitrixMonitor
        zopectl restart

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
