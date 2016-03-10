# -*- coding: utf-8 -*-


import nltk
import gensim
import codecs
import jieba
import re
import data


def segment(raw):
    """
    去除空白字符，停用词
    分词
    :param raw:
    :return list:
    """
    # 过滤空白字符
    # print raw
    blank_re = re.compile(r"\s+")
    raw_without_blank = blank_re.sub('', raw)
    # 分词
    seglist = jieba.cut(raw_without_blank, cut_all=False)
    # 去除停用词
    seg_without_stop = filter(lambda x: x not in data.stopwords, seglist)
    return seg_without_stop
