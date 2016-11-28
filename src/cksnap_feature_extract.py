#coding=utf-8
from sklearn import svm
from sklearn.externals import joblib
import numpy as np
from sklearn import  preprocessing

# cksnap 特征提取，调用 get_k_cksaap()即可得到特征，两个输入参数，1 为dna序列，2为k参数的值。返回dna序列相应的cksnap编码
class CkaapFeature:
    def __init__(self,template):
        self.template=template
    def get_list(self,k,res,ans,template):
        if len(res)==k:
            ans.append(res)
            return 
        for i in range(4):
            res+=template[i]
            self.get_list(k, res, ans, template)
            res=res[:len(res)-1]
        return ans
    def get_feature(self,seq,k=0):
        ans=[0]*16
        seq=seq.rstrip()
        length=len(seq)
        for i in range(length-k-1):
            tmp=seq[i]+seq[i+k+1]
            ls=self.get_list(2, '', [], self.template)
            index=ls.index(tmp)
            ans[index]+=1
        return ans
    def get__k_cksaap(self,seq,k):
        ans=[]
        for i in range(k):
            tmp_list=self.get_feature(seq, i)
            ans.extend(tmp_list)
        return ans  
 


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

ck=CkaapFeature(template='ACGT')

'''
　输入样本集、结果文件名字和k的值 得到样本集对应的cksnap编码

'''
def main(file_path, write_path, k=10):
    with open(file_path) as fr, open(write_path, 'w') as fw:
        for line in fr:
            line=line.strip('\n')  
            feature=ck.get__k_cksaap(line, k)
            write_list(feature, fw)


'''
对cksnap特征进行 标准化.   输入cksnap 特征文件格式，输出结果文件类型
'''

def normalize(file_name,des):
    data=np.loadtxt(file_name)
    res=preprocessing.normalize(data)
    np.savetxt(des,res)

if __name__=='__main__':
    print 'excuting...'
    sample_file='dataset.txt'
    ret_file='pre_nor.txt'
    k=15
    main(sample_file,ret_file,k)
    pre_normalize_file='pre_nor.txt'
    post_normalize_file='post_nor.txt'
    normalize(pre_normalize_file,post_normalize_file)
    '''
     最终post_normalize_file是得到的特征，将它和psdp合并即可。
    '''








