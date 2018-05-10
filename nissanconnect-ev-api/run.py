import logging
import sys
import main

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)



print ("hello")
username = "mark@perryman.org.uk"
password = "password"

logging.debug("login = %s , password = %s" % ( username , password)  )

print "Prepare Session"
s = main.Session(username, password , "NE")
print "Login..."
l = s.get_leaf()

leaf_info = l.get_latest_battery_status()

print "leaf_info.state_of_charge %s" % leaf_info.state_of_charge
