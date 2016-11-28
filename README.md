##TargetNUC说明

TargetNUC是目前核小体定位最精确的分类器，下面给出数据集和源码以及使用教程。

####1.数据集

1.H.sapiens  2273 个正样本  2300个负样本

2. C.elegans  2567个正样本   2608个负样本

3. D.melanogaster. 2900个正样本  2850负样本

所有样本中DNA序列长度都是147bp。

样本的下载地址在：http://lin.uestc.edu.cn/server/iNucPseKNC/dataset

处理好的数据集参考“数据集”文件夹。

####2代码说明

1．系统环境

软件： python2.7  numpy   scipy  scikit-learn

2.特征提取代码

参考“源代码文件夹”

1>cksnap_feature_extract.py 用于提取composition of k-spaced nucleic acid pairs 特征。 

2>psdp_feature_extract.py  用于提取 postion-specific deoxyribotide propensity 特征。

3>combine_feature.py 用于将两个特征合并

4>jack_knife_test.py 用于做jackknife测试， 使用的是svm分类器，参数选取使用的是libsvm。

5>k_validate_test.py 用于k-重交叉验证

注明：cksnap特征需要先正规化再和psdp特征合并，正规化的代码也在cksnap_feature_extract.py里面。Cksnap的k默认选为10.

####3.其他说明

1. 参数选择：  

H.sapiens数据集上 cksnap特征中K选15

C.elegans数据集上cksnap特征中K选10

D.melanogaster数据集上cksnap特征中K选10
          



