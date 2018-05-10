import requests
import json


class Point():
   def __init__(self, longitude, latitude):
       self.latitude = latitude
       self.longitude = longitude
   def __str__(self):
       return "({0}, {1})".format(self.longitude, self.latitude)


def getRoute(start, end):
    base_url = "http://www.yournavigation.org/api/1.0/gosmore.php?format=kml&flat=%s&flon=%s&tlat=%s&tlon=%s&v=motorcar&fast=1&layer=mapnik"
    getUrl = base_url % (start[0], start[1], end[0], end[1])
    website_text_result = requests.get(getUrl).text
    website_text_result = website_text_result.split("<coordinates> ")[1]
    website_text_result = website_text_result.split("</coordinates>")[0]
    coordinate_list = website_text_result.split("\n")
    new_coordinate_list = []
    for coordinate in coordinate_list:
        try:
            point = Point(float(coordinate.split(",")[0]), float(coordinate.split(",")[1]))
        except Exception:
            pass
        new_coordinate_list.append(point)
    
    return new_coordinate_list
