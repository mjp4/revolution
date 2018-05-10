import logging

logging.basicConfig(stream=sys.stdout, level=logging.ERROR)


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


class Session(object):

    def __init__(self, username, password, region="NE"):
        self.username = username
        self.password = password
        self.region_code = region
        self.logged_in = False
        self.custom_sessionid = None

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
