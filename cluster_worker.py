# -*- coding: utf-8 -*-

import src
import codecs

# 读入文件
input_file = codecs.open("data/genre/class/1_1.txt", 'rb', encoding='utf8')
raw = input_file.read()

# 分词
text_list = src.lsi.raw_init(raw)
# 生成文档向量
corpus = src.lsi.digitalize(text_list)
# 用tfidf训练
corpus_tfidf = src.lsi.build_tfidf(corpus)



input_file.close()
