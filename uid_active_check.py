#!/usr/bin/python3
import pymongo
import time
import csv
import sys
import os
from tqdm import tqdm

test_list = []

if __name__ == "__main__":
    f = open( sys.argv[1], "rt")
    m = []

    uidlist_txt_path = "/home/ethan/Desktop/uidlist.txt"
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

    activated_csv_file  = open("activated.csv", "w", newline='')
    activated_writer = csv.writer(activated_csv_file)

    nonactivated_csv_file  = open("nonactivated.csv", "w", newline='')
    nonactivated_writer = csv.writer(nonactivated_csv_file)

    for l in f:
        v = l.strip().split("\t")
        if len( v ) < 2:
            break;

        m.append( v[0] )

    counter = 0

    #activated = []
    #nonactive = []

    for uid in tqdm(m):

        found = False
        for x in mongo_coll.find({"key": uid}):
            found = True
            counter = counter + 1
        if found:
            #activated.append( uid )
            activated_writer.writerow([uid])
        else:
            #nonactive.append( uid )
            nonactivated_writer.writerow([uid])

    print (counter)
