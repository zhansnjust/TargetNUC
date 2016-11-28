#coding=utf-8
from sklearn import svm
from sklearn.externals import joblib
import numpy as np
from sklearn import  preprocessing


#把list写入文件，输入 list和 打开的文件流f
def write_list(ls,f):
    i=0
    while i<=len(ls)-1:
        if isinstance(ls[i], int):
            f.write(str(ls[i])+' ')
        elif isinstance(ls[i], float):
            f.write(str(ls[i])+' ')
        elif isinstance(ls[i], list):
            write_list(ls[i], f)
        else:
            f.write(ls[i]+' ')
        i=i+1
    f.write('\n')


#根据单个样本集，计算位置特异性核苷酸偏好特征，输入：特征文件 比如 正样本.txt
def get_mat(filepath):
    dataset=np.loadtxt(filepath, dtype=str)
    x=dataset.size #row
    print x
    y=len(dataset[0]) #column
    res=np.zeros([4,y])
    A=0.0
    C=0.0
    G=0.0
    T=0.0
    for i in xrange(y):
        for j in xrange(x):
            temp=dataset[j][i]
            if temp=='A':
                A+=1
            elif temp=='C':
                C+=1    
            elif temp=='G':
                G+=1
            else:
                T+=1
        res[0][i]=A/x
        res[1][i]=C/x
        res[2][i]=G/x
        res[3][i]=T/x
        A=0.0
        C=0.0
        G=0.0
        T=0.0
    return res



#根据位置特异性核苷酸偏好特征得到每个dna序列的特征信息, 输入：line表示一个dna序列，matx表示提取的psdp矩阵
def get_psdp_feature(line,matx):
    ans=[]
    length=len(line.strip())
    for i in xrange(length):
        temp=line[i]
        if temp=='A':
            ans.append(matx[0][i])
        elif temp=='C':
            ans.append(matx[1][i])
        elif temp=='G':
            ans.append(matx[2][i])
        elif temp=='T':
            ans.append(matx[3][i])
        else:
            print "error"
    return ans 

'''
输入正样本和负样本，得到最终psdp的结果。   其中输入的都是文件名 ，result也是文件，根据正负样本得到所有样本集的 psdp特征
'''
def main(postive_simple,negative_simple,result):
    positive_mat=get_mat(postive_simple)
    negative_mat=get_mat(negative_simple)
    mat=positive_mat-negative_mat
    with open(postive_simple) as fp,open(negative_simple) as fn,open(result,'w') as fw:
        for item in fp:
            if item=='\n':
                continue
            line=get_psdp_feature(item, mat)
            write_list(line,fw)
        for item in fn:
            line=get_psdp_feature(item, mat)
            write_list(line, fw)

if __name__ == '__main__':
    postive_simple='postive.txt'
    negative_simple='negative.txt'
    ret_file='psdp.txt'
    main(postive_simple,negative_simple,ret_file)
