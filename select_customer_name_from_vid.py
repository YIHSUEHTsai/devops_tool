#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import csv
import os
import sys
import pandas as pd

if __name__ == "__main__":
    while True:
        try:
            input_txt_file = str(input("\033[0;34m%s\033[0m" % "Please input vid list txt file name: "))
            output_txt_file = str(input("\033[0;34m%s\033[0m" % "Please input result txt file name: "))

        except ValueError:
            continue
        else:
            break

    #if os.path.isfile(input_txt_file):
    #    print("The input txt file is exist!")
    #else:
    #    print("[Error] The input txt file is not exist!")
    #    sys.exit()
   
    db = MySQLdb.connect(db='urp',host='192.168.5.213',user='analysis',passwd='eEtm9a3jHK9m6Umc',port=3306,charset='utf8')
    cursor = db.cursor()
    print('[Connect mysql]')

    file = open(input_txt_file+".txt", mode = 'r', encoding = 'utf-8-sig')
    fp = open(output_txt_file+".txt", "w")

    for line in file.readlines():
        vid = int(line,16)
        print (vid)
        cmd = "SELECT customer_name FROM urp_vid WHERE vid='" + str(vid) + "';"
        cursor.execute(cmd)

        fp.write(cursor.fetchall()[0][0]+"\n")

    fp.close()
    file.close()

    print('[parser finish]')
