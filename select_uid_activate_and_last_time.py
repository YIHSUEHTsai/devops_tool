#!/usr/bin/python3
import pymongo
import time
import csv
import sys
import os
from datetime import datetime
import json

test_list = []

if __name__ == "__main__": 
    while True:
        try:
            input_txt_file = str(input("\033[0;34m%s\033[0m" % "Please input uid list txt file name: "))
            output_txt_file = str(input("\033[0;34m%s\033[0m" % "Please input result txt file name: "))

        except ValueError:
            continue
        else:
            break

    db_name = 'ocean'
    coll_name = 'uid'
    url = "mongodb://{username}:{password}@{host}:{port}/{db_name}?authMechanism=MONGODB-CR".format(username='ocean',
                                                                       password='xhR81YjYvUkxJtNB',
                                                                       host='mongodb.tutk.com',
                                                                       port=7990,
                                                                       db_name='ocean')

    mongo_client = pymongo.MongoClient(url)
    mongo_db = mongo_client[db_name]
    mongo_coll = mongo_db[coll_name]

    csv_file  = open(output_txt_file+".csv", "w", newline='')
    writer = csv.writer(csv_file)
    writer.writerow(["uid", "activate_time", "last_time"])

    file = open(input_txt_file+".txt", mode = 'r', encoding = 'utf-8-sig')
    for line in file.readlines():
        uid = str(line)[0:20]
        print (uid)
        last_time = ""
        activate_time = ""

        for return_value in mongo_coll.find({"key": uid}):
            data = str(return_value)
            jsonStr = json.dumps(data)
            data = json.loads(jsonStr)

            for index in range(len(data.split(","))):
                #print (str(data.split(",")))

                if (str(data.split(",")[index]).find("last_time") != -1):
                    for data_index in range(len(str(data.split(",")[index]).split(" "))):
                        if (data_index+1 == len(str(data.split(",")[index]).split(" "))):
                            last_time = str(data.split(",")[index]).split(" ")[data_index]

                            #print (int(float(last_time.split("}",2)[0])))
                            last_time = datetime.fromtimestamp(int(float(last_time.split("}",2)[0])))

                elif (str(data.split(",")[index]).find("activate_time") != -1):
                    for data_index in range(len(str(data.split(",")[index]).split(" "))):
                        if (data_index+1 == len(str(data.split(",")[index]).split(" "))):
                            activate_time = str(data.split(",")[index]).split(" ")[data_index]
                            
                            print ((int(float(activate_time.split("}",2)[0]))))
                            activate_time = datetime.fromtimestamp(int(float(activate_time.split("}",2)[0])))

        writer.writerow([uid, activate_time, last_time])
   
