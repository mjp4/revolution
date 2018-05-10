import logging
import sys
import main
import time

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

def get_location(l):
    result_key = l.request_location()
    while True:
        location_status = l.get_status_from_location(result_key)
        if location_status is None:
            print "Waiting for response (sleep 10)"
            time.sleep(10)
        else:
            lat = location_status.latitude
            lon = location_status.longitude
            print("lat: {} long: {}".format(lat, lon))
            return lon, lat

username = "mark@perryman.org.uk"
password = "password"

print "Prepare Session"
s = main.Session(username, password , "NE")

print "Login..."
s = main.Session(username, password , "NE")

l = s.get_leaf()
longitude, lattitude = get_location(l)