

def main(self):
    username = "mark@perryman.org.uk"
    password = "password"

    logging.debug("login = %s , password = %s" % ( username , password)  )

    print "Prepare Session"
    s = pycarwings2.Session(username, password , "NE")
    print "Login..."
    l = s.get_leaf()

    print "leaf_info.state_of_charge %s" % leaf_info.state_of_charge

def get_latest_battery_status(self):



    response = self.session._request_with_retry("BatteryStatusRecordsRequest.php", {
        "RegionCode": self.session.region_code,
        "lg": self.session.language,
        "DCMID": self.session.dcm_id,
        "VIN": self.vin,
        "tz": self.session.tz,
        "TimeFrom": self.bound_time
    })
    if response["status"] == 200:
        return CarwingsLatestBatteryStatusResponse(response)

    return None
