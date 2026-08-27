#!/usr/bin/env python
# encoding: utf-8

# -*- coding: utf-8 -*-
# @contact: ybsdeyx@foxmail.com
# @software: PyCharm
# @time: 2019/3/6 9:59
# @author: Paulson●Wier
# @file: 5_词向量.py
# @desc:

# （1）Word2Vec

from gensim.models import Word2Vec
import jieba

# 定义停用词、标点符号
punctuation = ['、','）','（','，',",", "。", ":", ";", ".", "'", '"', "’", "?", "/", "-", "+", "&", "(", ")"]
sentences = [
    "长江是中国第一大河，干流全长6397公里（以沱沱河为源），一般称6300公里。流域总面积一百八十余万平方公里，年平均入海水量约九千六百余亿立方米。以干流长度和入海水量论，长江均居世界第三位。",
    "黄河，中国古代也称河，发源于中华人民共和国青海省巴颜喀拉山脉，流经青海、四川、甘肃、宁夏、内蒙古、陕西、山西、河南、山东9个省区，最后于山东省东营垦利县注入渤海。干流河道全长5464千米，仅次于长江，为中国第二长河。黄河还是世界第五长河。",
    "黄河,是中华民族的母亲河。作为中华文明的发祥地,维系炎黄子孙的血脉.是中华民族民族精神与民族情感的象征。",
    "黄河被称为中华文明的母亲河。公元前2000多年华夏族在黄河领域的中原地区形成、繁衍。",
    "在兰州的“黄河第一桥”内蒙古托克托县河口镇以上的黄河河段为黄河上游。",
    "黄河上游根据河道特性的不同，又可分为河源段、峡谷段和冲积平原三部分。 ",
    "黄河,是中华民族的母亲河。"
]

sentences = [jieba.lcut(sen) for sen in sentences]
print('sentences:\n',sentences)

# 去标点
tokenized = []
for sentence in sentences:
    words = []
    for word in sentence:
        if word not in punctuation:
            words.append(word)
    tokenized.append(words)
print('tokenized:\n',tokenized)

# 进行模型训练
model = Word2Vec(tokenized,sg=1,size=100,window=5,min_count=2,negative=1,sample=0.001,hs=1,workers=4)
'''
参数解释如下：

sg=1 是 skip-gram 算法，对低频词敏感；默认 sg=0 为 CBOW 算法。
size 是输出词向量的维数，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般值取为100到200之间。
window 是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b 个词，后面看 b 个词（b 在0-3之间随机）。

min_count 是对词进行过滤，频率小于 min-count 的单词则会被忽视，默认值为5。
negative 和 sample 可根据训练结果进行微调，sample 表示更高频率的词被随机下采样到所设置的阈值，默认值为 1e-3。
hs=1 表示层级 softmax 将会被使用，默认 hs=0 且 negative 不为0，则负采样将会被选择使用。

'''
model.save('model')  #保存模型
model = Word2Vec.load('model') #加载模型

#相似度
print(model.wv.similarity('黄河','长江'))
print(model.wv.most_similar(positive=['黄河','母亲河'],negative=['长江']))


# （2）Doc2Vec
# from gensim.models.doc2vec import Doc2Vec,LabeledSentence
# doc_labels = ["长江", "黄河", "黄河", "黄河", "黄河", "黄河", "黄河"]
# class LabeledLineSentence(object):
#     def __init__(self,doc_list,labels_list):
#         self.labels_list = labels_list
#         self.doc_list = doc_list
#
#     def __iter__(self):
#         for idx ,doc in enumerate(self.doc_list):
#             yield LabeledSentence(words=doc,tags=[self.labels_list[idx]])
#
#     # model = Doc2Vec(documents, dm=1, size=100, window=8, min_count=5, workers=4)
#     model = Doc2Vec(documents, dm=1, size=100, window=8, min_count=5, workers=4)
#     model.save('model1')
#     model = Doc2Vec.load('model1')
#
# iter_data = LabeledLineSentence(tokenized, doc_labels)
# model = Doc2Vec(dm=1, size=100, window=8, min_count=5, workers=4)
# model.build_vocab(iter_data)