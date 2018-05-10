from urllib.request import urlopen
import xml.etree.ElementTree as ET
import re as re


def getRoute(start, end):
    baseUrl = "http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&flat=%s&flon=%s&tlat=%s&tlon=%s&v=motorcar&fast=1&layer=mapnik"

    getUrl = baseUrl % (start[0], start[1], end[0], end[1])
    contents = urlopen(getUrl).read().decode('utf-8')
    #tree = ET.fromstring(contents)
    #coordinates = tree.iterfind('kml/Document/Folder/Placemark/LineString/coordinates').text
    #coordinates = root.findall("coordinates")
    regex = re.compile('<coordinates>.*</coordinates>')
    print(contents)
    coordinates = regex.search(contents).group()

    print(coordinates)




getRoute([51.652169, -0.084417],[55.950398, -3.180827])


# Enfield   51.652169, -0.084417
# Edinburgh  55.950398, -3.180827