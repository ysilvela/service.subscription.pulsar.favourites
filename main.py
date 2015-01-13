# coding: utf-8
import subscription
import xml.etree.ElementTree as ET
import re
import time
import xbmc

# this read the settings of add on
settings = subscription.Settings()

path = xbmc.translatePath('special://userdata')
tree = ET.parse("%sfavourites.xml" % path)
root = tree.getroot()

# check movies
listing = []
ID = []
for child in root:
    data = child.text
    if 'plugin://plugin.video.pulsar/movie' in data:
        listing.append(child.attrib['name'])
        ID.append(re.search('plugin://plugin.video.pulsar/movie/(.*?)/', data).group(1))
if len(listing) > 0:
    subscription.integration(listing, ID,'MOVIE', settings.movie_folder, True)


# check tv shows
listing = []
ID = []
for child in root:
    data = child.text
    if 'plugin://plugin.video.pulsar/show' in data:
        listing.append(child.attrib['name'])
        ID.append(re.search('plugin://plugin.video.pulsar/show/(.*?)/', data).group(1))
if len(listing) > 0:
    subscription.integration(listing, ID,'SHOW', settings.show_folder, True)