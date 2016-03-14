# -*- coding: utf-8 -*-
__author__ = 'zhiquan'

import re
import codecs

# input_file = codecs.open("data/source.txt", 'rb', encoding='utf8')

# 暂存无页眉页脚原始文本
# output_file = codecs.open("data/source_without_header.txt", 'wb', encoding='utf8')

# 去除页眉页脚
'''page_header_re = re.compile(u"普通高等.*专业介绍")
for line in input_file.readlines():
    if page_header_re.search(line):
        continue
    output_file.write(line)'''

# 按照学科大类分类存储
'''input_file = codecs.open("data/source_without_header.txt", 'rb', encoding='utf8')
counter = 0
output_file = codecs.open("data/genre/"+str(counter)+".txt", 'wb', encoding='utf8')
genre_re = re.compile(u"(\d\d)\s*学科门类")
for line in input_file.readlines():
    if genre_re.match(line):
        output_file.close()
        counter += 1
        if counter == 11:
            counter += 1
        output_file = codecs.open("data/genre/"+str(counter)+".txt", 'wb', encoding='utf8')
    output_file.write(line)'''

# 各学科小类别存储
index = (1, 13)
for counter in index:
    if counter == 11:
        continue
    counter

output_file.close()
input_file.close()
