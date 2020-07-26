#!/usr/bin/env python
# -*- coding: utf-8 -*-
import MySQLdb
import csv
import os
import sys

if __name__ == "__main__":
	while True:
		try:
			input_txt_file = str(raw_input("Please input uid list txt file name: "))
			print (input_txt_file)
			output_txt_file = str(raw_input("Please input result file name: "))

		except ValueError:
			continue
		else:
			break

	#db = MySQLdb.connect(db='urp',host='192.168.5.213',user='analysis',passwd='eEtm9a3jHK9m6Umc',port=3306)
	db = MySQLdb.connect(db='P2PDB',host='192.168.5.213',user='analysis',passwd='eEtm9a3jHK9m6Umc',port=3306)
	cursor = db.cursor()
	print('Connection OK')

	with open(input_txt_file+".txt",'r') as csvinput:
		with open(output_txt_file+".txt", 'wb') as csvoutput:
			writer = csv.writer(csvoutput,lineterminator=os.linesep)
			for rowreader in csv.reader(csvinput):
				if (len(rowreader) == 0):
					break

				print (rowreader)
				uid = rowreader[0]
				print (uid)
				#cursor.execute("SELECT CONV(urp_uid.active_vid, 10,16), CONV(urp_uid.active_pid, 10,16), CONV(urp_uid.active_gid, 10,16) FROM urp_uid WHERE uid='{0}';".format(uid))
				cursor.execute("SELECT CONV(DEV_Table.VID, 10,16), CONV(DEV_Table.PID, 10,16), CONV(DEV_Table.GID, 10,16) FROM DEV_Table WHERE uid='{0}';".format(uid))
				vid = cursor.fetchall()
				#print (vid)
				for row in vid:
					output = []
					for vid in range(len(row)):
						output.append(str(row[vid]))
						
					writer.writerow(rowreader+output)
				
		csvoutput.close()
		db.close()
