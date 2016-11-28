#coding=utf-8
'''
Created on 2016年4月13日

@author: Administrator
'''

import numpy as np

'''
合并两个特征， 输入两个特征文件格式，和返回的文件格式
'''
def main(feature1,feature2,result):
    m1=np.loadtxt(feature1)		
    m2=np.loadtxt(feature2)
    res=np.column_stack((m1,m2))
    np.savetxt(result,res)

if __name__ == '__main__':
    feature_file1='psdp.txt'
    feature_file2='post_nor.txt'
    main(feature_file1,feature_file2,'res.txt')