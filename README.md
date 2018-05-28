# FasterRcnnTF_ICPR2018
a Tensorflow version of Faster Rcnn for ICPR2018 text detection

It is a Tensorflow version of Faster Rcnn which is a very famous alg in object detection described by http://arxiv.org/pdf/1506.01497.pdf

I modify something and use it for a ICPR text detection competition hold by Aliyun & ICPR :https://tianchi.aliyun.com/competition/introduction.htm?spm=5176.100150.711.5.39862009x18lUE&raceId=231651

My work is based on endernewton's great work,also see installation and citation https://github.com/endernewton/tf-faster-rcnn

For normal object detection, my work got a mAp 71% at PASCAL VOC 2007 datasets

For text object detection mentioned before:

1. Transfer the datasets into the format like VOC_PASCAL
2. A icpr.py class file is used to carry the data as pascal_voc.py
3. K-means alg is used to chose the anchor ratio & size
4. Vertical-flip data augment is used
5. Much more iterations(200,000) is carry out for param convergence

Remain something not good enough for this work:

1. Faster Rcnn is mainly used for rectangular & horizontal object detection, but text objects in this competition are shape of non-
rectangular or non-horizontal, this work is not robust for such objects, and a sematic segmentation based method should be used.

2. The whole avaiable datasets are used as training data, results that no validation sets in this work. The official submission only has
3 chances, it's hard to valuate my module without a validation datasets.

Below is some of the results:

![exp0](https://github.com/superlich7/FasterRcnnTF_ICPR2018/blob/master/file/1304677279.jpg)

![exp0](https://github.com/superlich7/FasterRcnnTF_ICPR2018/blob/master/file/1391390647.jpg)

![exp0](https://github.com/superlich7/FasterRcnnTF_ICPR2018/blob/master/file/2029195364.jpg)
