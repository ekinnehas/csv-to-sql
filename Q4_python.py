#!/usr/bin/python

import csv
import MySQLdb

print("Enter  File  To Be Export")
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="mydb")
cursor = conn.cursor()
sql ='DROP TABLE IF EXISTS `MusicPortal`; CREATE TABLE MusicPortal (PLAY_ID char(32), SONG_ID int, CLIENT_ID int, PLAY_TS timestamp)'
cursor.execute(sql)

def convert(x):
    return "{}-{}-{} {}-{}-{}".format(x[6:10], x[3:5], x[0:2], x[11:13], x[14:16], x[17:19])

with open('filename') as csvfile:
    reader = csv.DictReader(csvfile, delimiter = '\t')

    for row in reader:
        print(row['PLAY_ID'], int(row['SONG_ID']), int(row['CLIENT_ID']), convert(row['PLAY_TS']))
        conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="", db="mydb")
        sql_statement = "INSERT INTO MusicPortal(PLAY_ID, SONG_ID, CLIENT_ID, PLAY_TS) VALUES (%s,%s,%s,%s)"
        cur = conn.cursor()
        cur.executemany(sql_statement,[(row['PLAY_ID'], int(row['SONG_ID']), int(row['CLIENT_ID']), convert(row['PLAY_TS']))])
        conn.escape_string(sql_statement)
conn.commit()
