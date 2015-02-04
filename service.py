import time

import xbmc
import xbmcaddon


def update_log():
    xbmc.log('[[script.subscription.pulsar.favourites] Update Favourites at %s' % time.asctime(
        time.localtime(previous_time)))
    xbmc.log('[[script.subscription.pulsar.favourites] Next Update in %s' % time.strftime("%H:%M:%S",
                                                                                           time.gmtime(every)))
    xbmc.executebuiltin('XBMC.Runaddon(script.subscription.pulsar.favourites)')


settings = xbmcaddon.Addon()
automatic = settings.getSetting('automatic')
delay_time = int(settings.getSetting('delay_time'))
if delay_time < 20: delay_time = 20
time.sleep(delay_time)  # it gives time to Pulsar to Start
every = 28800  # seconds
previous_time = time.time()
xbmc.log("[script.subscription.pulsar.favourites] Update Favourites List Service starting...")
xbmc.executebuiltin('XBMC.Runaddon(script.subscription.pulsar.favourites)')
update_log()
while (not xbmc.abortRequested) and automatic == 'true':
    if (time.time() > previous_time + every):  # verification
        previous_time = time.time()
        update_log()
    xbmc.sleep(500)
del settings
