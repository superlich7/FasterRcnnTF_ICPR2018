import os
import numpy as np
from sklearn.cluster import KMeans
from sklearn import metrics

X = np.array([],dtype = np.float)
n_cls = 4

fo = open('anchor_ratio.txt','r')

for line in fo:
    if float(line) < 1.0 :#and  float(line) > 3.0:
	    X = np.append(X,np.float(line))

X = X.reshape(-1,1)
#print(X)

y_pred = KMeans(n_clusters=n_cls).fit_predict(X)
score = metrics.calinski_harabaz_score(X,y_pred)
print(y_pred.shape)
#print('score = {}'.format(score))

for i in range(0,n_cls):
    cls_index = np.where(y_pred == i)
    X_value = X[cls_index]
    #X_mean = np.sum(X_value)/len(X_value)
    X_mean = np.mean(X_value)	
    #X_med = np.median(X_value)	
    #print('x index {}'.format(i))
    #print(cls_index)
    #print('x value {}'.format(i))
    #print(X_value)
    print('{}: x len = {:8f}, meam = {:8f}'.format(i,len(X_value),X_mean))

fo.close()
