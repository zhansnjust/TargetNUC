#coding=utf-8
'''
Created on 2016年4月9日

@author: Administrator
'''
import time
import numpy as np
import copy
from sklearn import svm
from sklearn import  cross_validation
from sklearn.ensemble import RandomForestClassifier
import random
from sklearn.cross_validation import StratifiedKFold
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
from sklearn import metrics

def cal(X,Y,clf):
    origin=[]
    predict=[]
    skf=StratifiedKFold(Y,10)
    index=1
    for train,test in skf:
        print "第",index,"次交叉验证"
        index+=1
        train_x=X[train]
        train_y=Y[train]
        test_x=X[test]
        test_y=Y[test]
        origin.extend(test_y)
        clf.fit(train_x,train_y)
        test_result=clf.predict(test_x)
        predict.extend(test_result)
    return origin,predict 

def get_evalution(predict,orgin):
    if len(predict)!=len(orgin):
        print 'evalution error'
        return 
    else:
        print 'predict序列:',predict
        tp=0
        tn=0
        fp=0
        fn=0
        se=0
        sp=0
        acc=0
        mcc=0
        length=len(predict)
        for i in xrange(length):
            if predict[i]>0.5:
                if orgin[i]==1:
                    tp+=1
                else:
                    fp+=1
            else:
                if orgin[i]==0:
                    tn+=1
                else:
                    fn+=1
        se=tp*1.0/(tp+fn)
        sp=tn*1.0/(tn+fp)
        acc=(tp+tn)*1.0/(tp+tn+fp+fn)
        mcc=(tp*tn-fp*fn)*1.0/((tp+fp)*(tp+fn)*(tn+fn)*(tn+fp))**0.5
        return se,sp,acc,mcc

if __name__=='__main__':
    import sys
    dataset=sys.argv[1]
    label=sys.argv[2]
    dataset=np.loadtxt(dataset)
    label=np.loadtxt(label)
    c=2
    gamm=2
    clf=svm.SVC(C=c,gamma=gamm)
    origin,result=cal(dataset, label, clf)
    se,sp,acc,mcc=get_evalution(result, origin)
    print 'se=',se,' sp=',sp,' acc=',acc,' mcc=',mcc
    
    