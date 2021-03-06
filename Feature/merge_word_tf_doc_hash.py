# -*- coding: utf-8 -*-
"""
@简介：将data_ensemble特征转换为稀疏矩阵，并将其合并到tfidf
@author: Jian
"""
import pickle
from scipy import sparse
from scipy.sparse import hstack

"""读取ensemble特征"""
f_1 = open('./data_doc2vec.pkl', 'rb')
x_train_1, y_train, x_test_1 = pickle.load(f_1)
f_1.close()

f_2 = open('./data_hash.pkl', 'rb')
x_train_2, _, x_test_2 = pickle.load(f_2)
f_2.close()

"""将numpy 数组 转换为 csr稀疏矩阵"""
x_train_1 = sparse.csr_matrix(x_train_1)
x_test_1 = sparse.csc_matrix(x_test_1)

x_train_2 = sparse.csr_matrix(x_train_2)
x_test_2 = sparse.csc_matrix(x_test_2)
"""读取tfidf特征"""
f_tfidf = open('./data_tf.pkl', 'rb')
x_train_3, _, x_test_3= pickle.load(f_tfidf)
f_tfidf.close()

"""对两个稀疏矩阵进行合并"""
x_train_4 = hstack([x_train_1, x_train_2])
x_test_4 = hstack([x_test_1, x_test_2])

x_train_5 = hstack([x_train_4, x_train_3])
x_test_5 = hstack([x_test_4, x_test_3])
"""将合并后的稀疏特征保存至本地"""
data = (x_train_5, y_train, x_test_5)
f = open('./merge_tf_doc_hash.pkl', 'wb')
pickle.dump(data, f)
f.close()




