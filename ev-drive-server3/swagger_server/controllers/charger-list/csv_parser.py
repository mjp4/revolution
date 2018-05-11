#!/usr/bin/python3

import csv
import json
import argparse

# name,latitude,longitude,town,postcode,deviceControllerName,chargeDeviceStatus,
# lastUpdated,paymentRequired,paymentRequiredDetails,subscriptionRequired,
# subscriptionRequiredDetails,connector1Type,connector1RatedOutputKW,connector1Status,
# connector2Type,connector2RatedOutputKW,connector2Status,connector3Type,
# connector3RatedOutputKW,connector3Status,connector4Type,connector4RatedOutputKW,
# connector4Status,connector5Type,connector5RatedOutputKW,connector5Status,connector6Type,
# connector6RatedOutputKW,connector6Status,connector7Type,connector7RatedOutputKW,
# connector7Status,connector8Type,connector8RatedOutputKW,connector8Status
USEFUL_DATA = [3, 4, 5, 13, 15, 27, 32, 38, 42, 43, 44, 45, 72, 73, 79, 83, 84,
               90, 94, 95, 101, 105, 106, 112, 116, 117, 123, 127, 128, 134, 138,
               139, 145, 149, 150, 156]
CHARGING_POINT_CONTROLLERS = ["Source London", "Chargemaster(POLAR)", "Charge Your Car",
                              "ChargePlace Scotland", "DBT", "POD Point", "Ecotricity",
                              "ChargePoint Services", "ABB", "Siemens", "CitiPark",
                              "Engenie", "No Controller"]
CHARGING_POINT_TYPES = ["Type 2 Mennekes", "CHAdeMO",
                        "Type 2 Combo", "Type 2 Tesla"]


def do_argparse():
    parser = argparse.ArgumentParser(description='How to filter the csv.')
    parser.add_argument("--functional",
                        dest="functional",
                        action="store_true",
                        help="Search for functional chargers only.")
    parser.add_argument("--device_controller",
                        dest="device_controller",
                        choices=CHARGING_POINT_CONTROLLERS,
                        help="Search for places with the specified device_controller",
                        action="store")
    parser.add_argument("--subscription_false",
                        dest="subscription_false",
                        help=("Search for places which don't require a subscription"),
                        action="store_true")
    parser.add_argument("--charger_type",
                        dest="charger_type",
                        choices=CHARGING_POINT_TYPES,
                        help=("Search based on a specifed charger type."),
                        action="store")
    args = parser.parse_args()
    return args


def main(args):
    with open("ev-drive-server3/swagger_server/controllers/charger-list/ncpr_list.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        firstrow = True
        listofdata = []
        listofdicts = []
        for row in spamreader:
                string1 = []
                if firstrow is True or charger_filters(row, args) is True:
                    for num in USEFUL_DATA:
                        string1.append(row[num-1])
                    listofdata.append(string1)

                    if not firstrow:
                        listofdicts.append(dict(
                            lat=row[3],
                            long=row[4],
                            network=row[26],
                            name=row[2],
                            other=','.join(string1)
                            ))
                    firstrow = False

        print("\n\n")
        with open("ev-drive-server3/swagger_server/controllers/charger-list/50over.csv", 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for item in listofdata:
                spamwriter.writerow(item)
        with open("ev-drive-server3/swagger_server/controllers/charger-list/50over.json", "w") as jsonfile:
            json.dump(listofdicts, jsonfile)


def filter_50kw(list1):
    KW_VALUES = [73, 84, 95, 106, 117, 128, 139, 150]
    for value in KW_VALUES:
        if value < len(list1) and list1[value-1] and int(round(float(list1[value-1]))) >= 50:
            return True
    return False


def filter_controller(list1, controller):
    if controller in " ".join(list1):
        return True
    else:
        return False


def filter_subscription(list1):
    if 43 < len(list1) and list1[43] == "0":
        return True
    else:
        return False


def filter_functional(list1):
    if 31 < len(list1) and list1[31] == "In service":
        return True
    else:
        return False


def filter_chargertype(list1, char_type):
    if char_type in " ".join(list1):
        return True
    else:
        return False


def charger_filters(list1, args):
    valid = []
    valid.append(filter_50kw(list1))
    if args.functional:
        valid.append(filter_functional(list1))
    if args.subscription_false:
        valid.append(filter_subscription(list1))
    if args.charger_type:
        valid.append(filter_chargertype(list1, args.charger_type))
    if args.device_controller:
        valid.append(filter_controller(list1, args.device_controller))
    if len(valid) == 0 or False not in valid:
        return True
    else:
        return False


if __name__ == "__main__":
    args = do_argparse()
    main(args)
    print("finished")
