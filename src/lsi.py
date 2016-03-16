# -*- coding: utf-8 -*-

import jieba
from data import stopwords
import re
import gensim


def raw_init(raw):
    """
    去除文本中的停用词，分词
    :param raw:
    :return 分词后的list,list中的元素为2级list,2级list中的元素为词。此时1级list中元素已经是未数字化的词向量:
    """

    # 去除空格符
    raw_without_space = re.sub('\s*', '', raw)
    # 将不同的专业分开作list元素
    # 专业号的正则表达式
    major_re = re.compile(u"\d\d\d\d\d\d")
    # 对整个字符串进行切片,分割符为此正则表达
    raw_splited = major_re.split(raw_without_space)

    # 分词
    raw_cut = map(lambda x: jieba.cut(x, cut_all=False), raw_splited)
    # 去除停用词
    raw_without_sw = map(lambda x: filter(lambda y: y not in stopwords, x), raw_cut)
    return raw_without_sw


def digitalize(raw):
    """
    此函数用于接受双层数组的中文文档，将其数字化为标准词向量
    :param raw: 此参数为一个双层数组，第一层每个元素为单个文档，第二层每个元素为文档中的词
    :return:    输入一个词向量
    """
    # 生成词袋
    dictionary = gensim.corpora.Dictionary(raw)
    # 生成文档向量
    corpus = [dictionary.doc2bow(text) for text in raw]
    return corpus


def build_lsi(raw):
    """
    :param raw: 此参数为一个文档向量,构成为[(0,n),(1,m),```]
    :return:    
    """


def build_tfidf(raw):
    """
    此函数用于接受一个文档向量并生成tf-idf模型，
    :param raw: 此参数为一个文档向量，构成为[(0,n),(1,m),```]
    :return: 经tf-idf模型训练后的文档向量，结构与参数相同
    """
    tfidf_model = gensim.models.TfidfModel(raw)
    corpus_tfidf = tfidf_model[raw]
    return corpus_tfidf
