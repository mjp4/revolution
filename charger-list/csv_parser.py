#!/usr/bin/python3

import csv

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


def main():
    with open("/home/ubuntu/hackathon/rEVolution/charger-list/ncpr_list.csv", newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
        firstrow = True
        listofdata = []
        for row in spamreader:
                string1 = []
                if firstrow is True or test_50kw(row) is True:
                    firstrow = False
                    for num in USEFUL_DATA:
                        string1.append(row[num-1])
                    listofdata.append(string1)
        print("\n\n")
        with open("/home/ubuntu/hackathon/rEVolution/charger-list/50over.csv", 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for item in listofdata:
                spamwriter.writerow(item)


def test_50kw(list1):
    KW_VALUES = [73, 84, 95, 106, 117, 128, 139, 150]
    for value in KW_VALUES:
        if value < len(list1) and list1[value-1] and int(round(float(list1[value-1]))) >= 50:
            return True
    return False


def test_ecotricity(list1):
    if "ecotricity" in " ".join(list1):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
    print("finished")
