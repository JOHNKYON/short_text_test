# -*- coding: utf-8 -*-

import src
import codecs
import conf

# 读入文件
input_file = codecs.open("data/genre/class/1_1.txt", 'rb', encoding='utf8')
raw = input_file.read()

# 分词
# conf.jieba_conf.init()
text_list = src.lsi.raw_init(raw)

# 生成文档向量
dic_corpus = src.lsi.digitalize(text_list)
dictionary = dic_corpus[0]
corpus = dic_corpus[1]

# 用tfidf训练
corpus_tfidf = src.lsi.build_tfidf(corpus)

# 训练lsi模型
lsi = src.lsi.build_lsi(corpus_tfidf, dictionary)

# 获取索引
index = src.lsi.lsi_index(lsi, corpus)

# 用索引和语料库生成关联度矩阵
src.lsi.sim_matrix(index)


input_file.close()
