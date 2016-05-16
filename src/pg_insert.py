# -*- coding:utf-8 -*-

import codecs
import json
import psycopg2

__author__ = "JOHNKYON"


def pg_insert(bucket, pg_conf):
    """
    灌入major_bucket至postgresql
    :param bucket:
    :return:
    """
    input_file = codecs.open("data/major_dict.json", 'rb', encoding='utf8')
    major_list = input_file.read()
    dic = json.loads(major_list)
    bucket = map(lambda x: (dic[str(x[0])], x[1], x[2]), bucket)

    connect = psycopg2.connect(database=pg_conf['database'], user=pg_conf['user'], password=pg_conf['password'],
                               host=pg_conf['host'], port=pg_conf['port'])

    cursor = connect.cursor()

    for ele in bucket:
        cursor.execute("INSERT INTO major_bucket VALUES(%s, %s, %s)", ele)

    connect.commit()
    cursor.close()
    connect.close()

    input_file.close()
