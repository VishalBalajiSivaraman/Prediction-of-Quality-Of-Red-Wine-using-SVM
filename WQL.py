# -*- coding: utf-8 -*-
"""Untitled38.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1D8Trl4wwfawf_9i_HM6zq7lHgGVmKLTv
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset=pd.read_csv('winequality-red.csv')
dataset.dropna(how='any')
dataset['Overall Acidity']=(dataset['fixed acidity']+dataset['volatile acidity'])/2
dataset['Overall Sulfur Dioxide']=(dataset['free sulfur dioxide']+dataset['total sulfur dioxide'])/2
dataset['Quality']=dataset['quality']
df=dataset.drop(columns=['fixed acidity','volatile acidity','free sulfur dioxide','total sulfur dioxide','quality'])
df

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

Y=Y.reshape(len(Y),1)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.25,random_state=0)

from sklearn.svm import SVC
svc=SVC(kernel='linear',random_state=0)
svc.fit(X_train,Y_train)

y_pred = svc.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), Y_test.reshape(len(Y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(Y_test, y_pred)
print(cm)
print(accuracy_score(Y_test, y_pred)*100)