# -*- coding: utf-8 -*-

import codecs
import re

input_file = codecs.open("data/source_without_header.txt", 'rb', encoding='utf8')
output_file = codecs.open("data/major_list.txt", 'wb', encoding='utf8')

major_re = re.compile(u"\d\d\d\d\d\d")
counter = 0


for line in input_file.readlines():
    if major_re.match(line):
        output_file.write(str(counter) + "\t" + line)
        counter += 1

input_file.close()
output_file.close()
