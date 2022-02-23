import numpy as np
from geneticalgorithm import geneticalgorithm as ga

"""
python tutorial for geneticalgorithm module

https://pypi.org/project/geneticalgorithm/
https://pypi.org/project/geneticalgorithm/#1111-id

do not forget to check the list of parameters , and what each one of them means .

Created on Thu Dec 23 01:23:40 2021

@author: essam

"""


def f(X):
    c=0
    for i in range(8):
        h=1
        for j in range(i,8):
            if i==j:
                continue
            if X[i]==X[j]:
                c+=1
            elif abs(X[i]-X[j])==h:
                c+=1
            h+=1    

    return c

varbound=np.array([[0,7]]*8)

model=ga(function=f,dimension=8,variable_type='int',variable_boundaries=varbound,function_timeout=15)

model.run()
