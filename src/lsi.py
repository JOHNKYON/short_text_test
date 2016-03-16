# -*- coding: utf-8 -*-

import jieba
from data import stopwords
import re


def raw_init(raw):
    """
    去除文本中的停用词，分词
    :param raw:
    :return 分词后的list,list中的元素为2级list,2级list中的元素为词。此时1级list中元素已经是未数字化的词向量:
    """

    # 将不同的专业分开作list元素
    # 专业号的正则表达式
    major_re = re.compile(u"\d\d\d\d\d\d")
    # 对整个字符串进行切片,分割符为此正则表达
    raw_splited = major_re.split(raw)
    print raw_splited

    '''
    # 分词
    raw_cut = jieba.cut(raw, cut_all=False)
    # 去除停用词
    raw_without_sw = filter(lambda x: x not in stopwords, raw_cut)
    print raw_without_sw
'''