import requests
from requests import Request, Session, RequestException
import json
import logging
from datetime import date
import base64
from Crypto.Cipher import Blowfish
import binascii
import time
from ConfigParser import SafeConfigParser
import sys
import pprint

import logging
from datetime import date, timedelta, datetime

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)

BASE_URL = "https://gdcportalgw.its-mo.com/gworchest_160803A/gdc/"

log = logging.getLogger(__name__)

def main(self):
    username = "mark@perryman.org.uk"
    password = "password"

    logging.debug("login = %s , password = %s" % ( username , password)  )

    print "Prepare Session"
    s = pycarwings2.Session(username, password , "NE")
    print "Login..."
    l = s.get_leaf()

    leaf_info = l.get_latest_battery_status()

    print "leaf_info.state_of_charge %s" % leaf_info.state_of_charge

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

def _PKCS5Padding(string):
    byteNum = len(string)
    packingLength = 8 - byteNum % 8
    appendage = chr(packingLength) * packingLength
    return string + appendage

class Session(object):

    def __init__(self, username, password, region="NE"):
        self.username = username
        self.password = password
        self.region_code = region
        self.logged_in = False
        self.custom_sessionid = None

    def _request_with_retry(self, endpoint, params):
        ret = self._request(endpoint, params)

        if ("status" in ret) and (ret["status"] >= 400):
            log.error("carwings error; logging in and trying request again: %s" % ret)
            # try logging in again
            self.connect()
            ret = self._request(endpoint, params)

        return ret

    def _request(self, endpoint, params):
        params["initial_app_strings"] = "geORNtsZe5I4lRGjG9GZiA"
        if self.custom_sessionid:
            params["custom_sessionid"] = self.custom_sessionid
        else:
            params["custom_sessionid"] = ""

        req = Request('POST', url=BASE_URL + endpoint, data=params).prepare()

        log.debug("invoking carwings API: %s" % req.url)
        log.debug("params: %s" % json.dumps(params, sort_keys=True, indent=3, separators=(',', ': ')))

        try:
            sess = requests.Session()
            response = sess.send(req)
            log.debug('Response HTTP Status Code: {status_code}'.format(
                status_code=response.status_code))
            log.debug('Response HTTP Response Body: {content}'.format(
                content=response.content))
        except RequestException:
            log.warning('HTTP Request failed')

        j = json.loads(response.content)

        if "message" in j and j["message"] == "INVALID PARAMS":
            log.error("carwings error %s: %s" % (j["message"], j["status"]) )
            raise CarwingsError("INVALID PARAMS")
        if "ErrorMessage" in j:
            log.error("carwings error %s: %s" % (j["ErrorCode"], j["ErrorMessage"]) )
            raise CarwingsError

        return j

    def connect(self):
        self.custom_sessionid = None
        self.logged_in = False

        response = self._request("InitialApp.php", {
            "RegionCode": self.region_code,
            "lg": "en-US",
        })
        ret = CarwingsInitialAppResponse(response)

        c1  = Blowfish.new(ret.baseprm, Blowfish.MODE_ECB)
        packedPassword = _PKCS5Padding(self.password)
        encryptedPassword = c1.encrypt(packedPassword)
        encodedPassword = base64.standard_b64encode(encryptedPassword)

        response = self._request("UserLoginRequest.php", {
            "RegionCode": self.region_code,
            "UserId": self.username,
            "Password": encodedPassword,
        })

        ret = CarwingsLoginResponse(response)

        self.custom_sessionid = ret.custom_sessionid

        self.gdc_user_id = ret.gdc_user_id
        log.debug("gdc_user_id: %s" % self.gdc_user_id)
        self.dcm_id = ret.dcm_id
        log.debug("dcm_id: %s" % self.dcm_id)
        self.tz = ret.tz
        log.debug("tz: %s" % self.tz)
        self.language = ret.language
        log.debug("language: %s" % self.language)
        log.debug("vin: %s" % ret.vin)
        log.debug("nickname: %s" % ret.nickname)

        self.leaf = Leaf(self, ret.leafs[0])

        self.logged_in = True

        return ret

    def get_leaf(self, index=0):
        if not self.logged_in:
            self.connect()

        return self.leaf


class Leaf:
    def __init__(self, session, params):
        self.session = session
        self.vin = params["vin"]
        self.nickname = params["nickname"]
        self.bound_time = params["bound_time"]
        log.debug("created leaf %s/%s" % (self.vin, self.nickname))

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

    def request_location(self):
        response = self.session._request_with_retry("MyCarFinderRequest.php", {
            "RegionCode": self.session.region_code,
            "lg": self.session.language,
            "DCMID": self.session.dcm_id,
            "VIN": self.vin,
            "tz": self.session.tz,
            "UserId": self.session.gdc_user_id, # this userid is the 'gdc' userid
        })
        return response["resultKey"]

    def get_status_from_location(self, result_key):
        response = self.session._request_with_retry("MyCarFinderResultRequest.php", {
            "RegionCode": self.session.region_code,
            "lg": self.session.language,
            "DCMID": self.session.dcm_id,
            "VIN": self.vin,
            "tz": self.session.tz,
            "resultKey": result_key,
        })
        if response["responseFlag"] == "1":
            return MyCarFinderResponse(response)

        return None

class CarwingsResponse:
    def __init__(self, response):
        op_result = None
        if ("operationResult" in response):
            op_result = response["operationResult"]
        elif ("OperationResult" in response):
            op_result = response["OperationResult"]

        # seems to indicate that the vehicle cannot be reached
        if ( "ELECTRIC_WAVE_ABNORMAL" == op_result):
            log.error("could not establish communications with vehicle")
            raise pycarwings2.CarwingsError("could not establish communications with vehicle")

    def _set_cruising_ranges(self, status, off_key="cruisingRangeAcOff", on_key="cruisingRangeAcOn"):
        self.cruising_range_ac_off_km = float(status[off_key]) / 1000
        self.cruising_range_ac_on_km = float(status[on_key]) / 1000

    def _set_timestamp(self, status):
        self.timestamp = datetime.strptime(status["timeStamp"], "%Y-%m-%d %H:%M:%S") # "2016-01-02 17:17:38"

class CarwingsInitialAppResponse(CarwingsResponse):
    def __init__(self, response):
        CarwingsResponse.__init__(self, response)
        self.baseprm = response["baseprm"]

class CarwingsLoginResponse(CarwingsResponse):
    def __init__(self, response):
        CarwingsResponse.__init__(self, response)

        profile = response["vehicle"]["profile"]
        self.gdc_user_id = profile["gdcUserId"]
        self.dcm_id = profile["dcmId"]
        self.vin = profile["vin"]

        # vehicleInfo block may be top level, or contained in a VehicleInfoList object;
        # why it's sometimes one way and sometimes another is not clear.
        if "VehicleInfoList" in response:
            self.nickname = response["VehicleInfoList"]["vehicleInfo"][0]["nickname"]
            self.custom_sessionid = response["VehicleInfoList"]["vehicleInfo"][0]["custom_sessionid"]
        elif "vehicleInfo" in response:
            self.nickname = response["vehicleInfo"][0]["nickname"]
            self.custom_sessionid = response["vehicleInfo"][0]["custom_sessionid"]

        customer_info = response["CustomerInfo"]
        self.tz = customer_info["Timezone"]
        self.language = customer_info["Language"]
        self.user_vehicle_bound_time = customer_info["VehicleInfo"]["UserVehicleBoundTime"]

        self.leafs = [ {
            "vin": self.vin,
            "nickname": self.nickname,
            "bound_time": self.user_vehicle_bound_time
        } ]

class CarwingsLatestBatteryStatusResponse(CarwingsResponse):
    def __init__(self, status):
        CarwingsResponse.__init__(self, status["BatteryStatusRecords"])

        self.answer = status

        recs = status["BatteryStatusRecords"]

        bs = recs["BatteryStatus"]
        self.battery_capacity = bs["BatteryCapacity"]
        self.battery_remaining_amount = bs["BatteryRemainingAmount"]
        self.charging_status = bs["BatteryChargingStatus"]
        self.is_charging = ("NOT_CHARGING" != bs["BatteryChargingStatus"]) # double negatives are fun
        self.is_quick_charging = ("RAPIDLY_CHARGING" == bs["BatteryChargingStatus"])

        self.plugin_state = recs["PluginState"]
        self.is_connected = ("NOT_CONNECTED" != recs["PluginState"]) # another double negative, for the kids
        self.is_connected_to_quick_charger = ("QC_CONNECTED" == recs["PluginState"])

        self._set_cruising_ranges(recs, off_key="CruisingRangeAcOff", on_key="CruisingRangeAcOn")

        if "TimeRequiredToFull" in recs:
            self.time_to_full_trickle = timedelta(minutes=_time_remaining(recs["TimeRequiredToFull"]))
        else:
            self.time_to_full_trickle = None

        if "TimeRequiredToFull200" in recs:
            self.time_to_full_l2 = timedelta(minutes=_time_remaining(recs["TimeRequiredToFull200"]))
        else:
            self.time_to_full_l2 = None

        if "TimeRequiredToFull200_6kW" in recs:
            self.time_to_full_l2_6kw = timedelta(minutes=_time_remaining(recs["TimeRequiredToFull200_6kW"]))
        else:
            self.time_to_full_l2_6kw = None

        self.battery_percent = 100 * float(self.battery_remaining_amount) / float(self.battery_capacity)

        # Leaf 2016 has SOC (State Of Charge) in BatteryStatus, a more accurate battery_percentage
        if "SOC" in bs:
            self.state_of_charge = bs["SOC"]["Value"]
            # optional?
            #self.battery_percent = self.soc
        else:
            self.state_of_charge = None

def _time_remaining(t):
    minutes = float(0)
    if t:
        if ("hours" in t) and t["hours"]:
            minutes = 60*float(t["hours"])
        elif ("HourRequiredToFull" in t) and t["HourRequiredToFull"]:
            minutes = 60*float(t["HourRequiredToFull"])
        if ("minutes" in t) and t["minutes"]:
            minutes += float(t["minutes"])
        elif ("MinutesRequiredToFull" in t) and t["MinutesRequiredToFull"]:
            minutes += float(t["MinutesRequiredToFull"])

    return minutes

class MyCarFinderResponse(CarwingsResponse):
    def __init__(self, status):
        CarwingsResponse.__init__(self, status)

        self.latitude = status["lat"]
        self.longitude = status["lng"]