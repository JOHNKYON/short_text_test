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
index = range(1, 14)
counter2 = 0    # 用于存储小类编号
class_re = re.compile(u"\d\d\d\d *.*类")
if class_re.match(u"0101 哲学类"):
    print "ok"
# 初始化状态
output_file = codecs.open("data/genre/class/1_0.txt", 'wb', encoding='utf8')

# 遍历每个大类
for counter in index:
    counter2 = 0
    if counter == 11:
        continue
    input_file = codecs.open("data/genre/"+str(counter)+".txt", 'rb', encoding='utf8')
    for line in input_file.readlines():
        if class_re.match(line):
            output_file.close()
            counter2 += 1
            output_file = codecs.open("data/genre/class/"+str(counter)+'_'+str(counter2)+'.txt', 'wb', encoding='utf8')
        output_file.write(line)
    input_file.close()
