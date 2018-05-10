import logging
import sys
import main

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)
username = "mark@perryman.org.uk"
password = "password"

if __name__ == "__main__":
    print "Executing run.py"

    print "Prepare Session"
    s = main.Session(username, password , "NE")

    print "Login..."
    l = s.get_leaf()

    leaf_info = l.get_latest_battery_status()
    print "leaf_info.state_of_charge %s" % leaf_info.state_of_charge

    longitude, lattitude = main.get_location(l)
