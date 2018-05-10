from flask import Flask, request, session, make_response
import random
import json
from time import sleep, time
from threading import Thread
from sqltea import Database
# import (whatever Rob's module is called)

MATCH_TIMEOUT = 1800
WAIT_TIMEOUT = 1800

app = Flask(__name__)

pairings = {}

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    print "in submit"
    if request.method == 'POST':
        name = request.form['name']
        initials = request.form['initials']
        office = request.form['office']
    elif request.method == 'GET':                    # only for testing
        name = request.args['name']
        initials = request.args['initials']
        office = request.args['office']


    session['initials'] = initials
    is_matched = 0


    matches = [inits for inits in app_db.select(office, 10)
        if inits!=initials]

    print matches

    if matches:
        match_initials = random.choice(matches)
        match_time = time()

        pairings[initials] = (match_initials, match_time)
        pairings[match_initials] = (initials, match_time)

        app_db.update_keen(initials, False)
        app_db.update_keen(match_initials, False)
        is_matched = 1

    else:
        app_db.insert_employee(initials, name, office)
        app_db.update_keen(initials, True)

    resp = make_response(str(is_matched))
    resp.mimetype = "application/json"

    return resp


@app.route('/check', methods=['GET'])
def check():
    print "in check"
    print session['initials']
    is_matched = 0
    if session['initials'] in pairings.keys():
        is_matched = 1
    resp = make_response(str(is_matched))
    resp.mimetype = "application/json"
    return resp
    
@app.route('/match', methods=['GET'])
def get_match():
    print pairings
    partner_initials, _ = pairings[session['initials']]
    data = {
        'success' : True,
        'partner' : partner_initials
        }

    resp = make_response(json.dumps(data))
    resp.mimetype = "application/json"
    return resp


# call this in a separate thread
def update_timeouts():
    while True:
        # remove old matches
        for key, val in pairings.items():
            if time() - val[1] > MATCH_TIMEOUT:
                del pairings[key]
        sleep(5)

# for testing
@app.route('/dump', methods=['GET'])
def dump():
    return str(pairings)

# for testing
@app.route('/clear', methods=['GET'])
def clear():
    pairings = {}
    return str(pairings)


if __name__== '__main__':
    app.secret_key = '\x9d\xd3\xe8\xb0\x90V\xf9\xeb\x0c\xf1d\xe2g\x82\r\x92\xce\x01\xa4\xecq<\x9c\x82'
    global app_db
    app_db = Database("Tea.db")
    
    t= Thread(target=update_timeouts, args = ())
    t.start()

    app.run('localhost', port=80)


