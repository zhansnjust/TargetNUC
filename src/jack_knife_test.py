#coding:utf-8
import numpy as np
from sklearn import svm
import copy
from time import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

#import sys
#===============================================================================
# train_set=dataset[:-1,:]
# pre_set=dataset[-1]
# train_y=lable[:-1]
# clf=svm.LinearSVC()
# clf.fit(train_set, train_y)
# print clf.predict(pre_set)
#===============================================================================

def jack_knife(data_set,label_=None):
    ans=[]
    len_row=data_set.shape[0]
    for i in xrange(len_row):
        print 'svm jack knife the:',i+1,'sample'
        train_data1=data_set[0:i,:]
        train_data2=data_set[i+1:,:]
        train_data=np.row_stack((train_data1,train_data2))
        #深拷贝的目的就是为了防止程序修改了label_ ;label_每个循环都要用
        train_label=copy.deepcopy(label_)
        del train_label[i]
        predict_data=data_set[i]
        #此处修改分类器,SVC中的  C和gmma可以通过libsvm得到。 这种jack_knife速度比较快
        #注意： SVC预测的结果是1和0，SVR预测的结果是小数，大于0.5为正类，否则是负类
        clf=svm.SVC(C=8,gamma=0.125)
#         clf=DecisionTreeClassifier()
#         clf=RandomForestClassifier(n_estimators=35,max_features=1280,max_depth=None)
        clf.fit(train_data, train_label)
        result=clf.predict(predict_data)
        ans.append(result[0])
    return ans

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
        print 'tp=',tp,' tn=',tn,' fp=',fp,' fn=',fn
        se=tp*1.0/(tp+fn)
        sp=tn*1.0/(tn+fp)
        acc=(tp+tn)*1.0/(tp+tn+fp+fn)
        mcc=(tp*tn-fp*fn)*1.0/((tp+fp)*(tp+fn)*(tn+fn)*(tn+fp))**0.5
        return se,sp,acc,mcc
    
if __name__=='__main__':
    print 'excuting...'
    #命令行下运行python文件，第一个参数是样本，第二个是类标
    import sys
    data_file=sys.argv[1]
    label_file=sys.argv[2]
    label=list(label_file)
    ans=jack_knife(data_file, label)
    se,sp,acc,mcc=get_evalution(ans, label)
    print 'se=',se,' sp=',sp,' acc=',acc,' mcc=',mcc
