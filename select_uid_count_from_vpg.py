#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import MySQLdb
import csv
import os
import sys
import pandas as pd

db = MySQLdb.connect(db='urp',host='192.168.5.213',user='analysis',passwd='eEtm9a3jHK9m6Umc',port=3306)
cursor = db.cursor()
print('Connection OK')

if __name__ == "__main__":
	while True:
		try:
			input_csv_file = str(input("\033[0;34m%s\033[0m" % "Please input uid list csv file name: "))
			print (input_csv_file)
			output_csv_file = str(input("\033[0;34m%s\033[0m" % "Please input uid list csv file name: "))

		except ValueError:
			continue
		else:
			break

	output_csv_file = open(output_csv_file+".csv", 'w', newline='')
	writer = csv.writer(output_csv_file)
	writer.writerow(['customer_name', 'p2pserver_ip', 'vid', 'pid', 'gid', 'uid_count'])

	input_csv_data = pd.read_csv(input_csv_file+".csv")

	for index in range(len(input_csv_data['customer_name'])):
		customer_name = input_csv_data['customer_name'][index]
		p2pserver_ip = input_csv_data['p2pserver_ip'][index]
		vid_hex = input_csv_data['vid'][index]
		pid_hex = input_csv_data['pid'][index]
		gid_hex = input_csv_data['gid'][index]

		vid = int(vid_hex,16)
		pid = int(pid_hex,16)
		gid = int(gid_hex,16)


		db_cmd = "SELECT count(uid) FROM urp_uid WHERE active_vid=" + str(vid) + " and active_pid=" + str(pid) + " and active_gid =" + str(gid)
		cursor.execute(db_cmd)
		uid_count = cursor.fetchall()
		
		print (customer_name," ",p2pserver_ip," ",vid_hex," ", pid_hex, " ", gid_hex," ",uid_count)	
		writer.writerow([customer_name, p2pserver_ip, vid_hex, pid_hex, gid_hex, uid_count])
	
