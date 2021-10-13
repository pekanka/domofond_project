import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import metrics
from sklearn import cluster
import _pickle as cPickle

def pr_dest(a, slc):
    a = np.array(a)
    ll = []
    if len(a.shape) == 1:
        a = [a]
    for i in a:
        ll.append(slc.predict(i.reshape(1, -1))[0])
    return(np.array(ll))