# -*- coding: utf-8 -*-

import src
import codecs

# 读入文件
input_file = codecs.open("data/genre/class/1_1.txt", 'rb', encoding='utf8')
raw = input_file.read()

src.lsi.raw_init(raw)

input_file.close()
