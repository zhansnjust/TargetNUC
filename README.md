##TargetNUC˵��

TargetNUC��Ŀǰ��С�嶨λ�ȷ�ķ�����������������ݼ���Դ���Լ�ʹ�ý̡̳�

####1.���ݼ�

1.H.sapiens  2273 ��������  2300��������

2. C.elegans  2567��������   2608��������

3. D.melanogaster. 2900��������  2850������

����������DNA���г��ȶ���147bp��

���������ص�ַ�ڣ�http://lin.uestc.edu.cn/server/iNucPseKNC/dataset

����õ����ݼ��ο������ݼ����ļ��С�

####2����˵��

1��ϵͳ����

����� python2.7  numpy   scipy  scikit-learn

2.������ȡ����

�ο���Դ�����ļ��С�

1>cksnap_feature_extract.py ������ȡcomposition of k-spaced nucleic acid pairs ������ 

2>psdp_feature_extract.py  ������ȡ postion-specific deoxyribotide propensity ������

3>combine_feature.py ���ڽ����������ϲ�

4>jack_knife_test.py ������jackknife���ԣ� ʹ�õ���svm������������ѡȡʹ�õ���libsvm��

5>k_validate_test.py ����k-�ؽ�����֤

ע����cksnap������Ҫ�����滯�ٺ�psdp�����ϲ������滯�Ĵ���Ҳ��cksnap_feature_extract.py���档Cksnap��kĬ��ѡΪ10.

####3.����˵��

1. ����ѡ��  

H.sapiens���ݼ��� cksnap������Kѡ15

C.elegans���ݼ���cksnap������Kѡ10

D.melanogaster���ݼ���cksnap������Kѡ10
          



