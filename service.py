import xbmc
import time
import os


def update_log():
    xbmc.log('[[service.subscription.pulsar.favourites] Update Favourites at %s' % time.asctime(
        time.localtime(previous_time)))
    xbmc.log('[[service.subscription.pulsar.favourites] Next Update in %s' % time.strftime("%H:%M:%S",
                                                                                           time.gmtime(every)))
    xbmc.executebuiltin('XBMC.Runaddon(service.subscription.pulsar.favourites)')


time.sleep(20) #it gives time to Pulsar to Start
every = 28800 # seconds
previous_time = time.time()
xbmc.log("[service.subscription.pulsar.favourites] Update Favourites List Service starting...")
xbmc.executebuiltin('XBMC.Runaddon(service.subscription.pulsar.favourites)')
update_log()
while (not xbmc.abortRequested):
    if (time.time() > previous_time + every):  #verification
        previous_time = time.time()
        update_log()
    xbmc.sleep(500)
