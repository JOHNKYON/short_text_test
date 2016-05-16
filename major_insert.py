# -*- coding:utf-8 -*-

import codecs
import json
import psycopg2

__author__ = "JOHNKYON"

input_file = codecs.open("data/major_dict.json", "rb", encoding='utf8')

raw = input_file.read()

connect = psycopg2.connect(database="dodo", user="data", password="wjf721", host="101.201.183.135", port=3433)

cursor = connect.cursor()

dic = json.loads(raw)

for a in range(0, 506):
    para = [dic[str(a)]]
    cursor.execute("INSERT INTO major (name) VALUES (%s)", para)

connect.commit()
cursor.close()
connect.close()

input_file.close()