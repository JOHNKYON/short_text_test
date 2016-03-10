# -*- coding: utf-8 -*-

import segment
import codecs

input_file = codecs.open("data/source.txt", 'rb', encoding='utf8')
output_file = codecs.open("data/seg_test.txt", 'wb', encoding='utf8')

raw = input_file.read()

text = segment.segment(raw)
output_file.write('\t'.join(text))

input_file.close()
output_file.close()
