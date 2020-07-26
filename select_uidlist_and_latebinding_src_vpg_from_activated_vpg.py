#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import csv
import os
import sys

db = MySQLdb.connect(db='urp',host='192.168.5.213',user='analysis',passwd='eEtm9a3jHK9m6Umc',port=3306)
cursor = db.cursor()
print('Connection OK')

if __name__ == "__main__":
	while True:
		try:
			vid = str(input("\033[0;34m%s\033[0m" % "$Please enter vid: "))
			pid = str(input("\033[0;34m%s\033[0m" % "$Please enter pid: "))
			gid = str(input("\033[0;34m%s\033[0m" % "$Please enter gid: "))
		except ValueError:
			continue
		else:
			break

	file_name = vid + "_" + pid + "_" + gid + ".csv"

	vid = int(vid,16)
	pid = int(pid,16)
	gid = int(gid,16)
	print ("vpg:", vid, pid, gid)

	output_csv_file = open(file_name, 'w', newline='')
	writer = csv.writer(output_csv_file)

	writer.writerow(["uid","vid","pid","gid","active_vid","active_pid","active_gid"])
	db_cmd = "SELECT uid,vid,pid,gid FROM urp_uid WHERE active_vid=" + str(vid) + " and active_pid=" + str(pid) + " and active_gid =" + str(gid)

	print (db_cmd)
 
	cursor.execute(db_cmd)

	uid = cursor.fetchall()

	for row in uid:
		output = []
		for uid in range(len(row)):
			output.append(str(row[uid]))
			
		writer.writerow([output[0],hex(int(str(output[1]),10)),output[2],output[3],hex(int(str(vid),10)),hex(int(str(pid),10)),hex(int(str(gid),10))])
	
