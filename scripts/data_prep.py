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


def dta_metro(a):
    with open("models/metro_enc.pkl", "rb") as f:
        enc = cPickle.load(f)
    ohe = []
    for i in range(len(a)):
        ohe.append(enc.transform([[a[i][0]]]).toarray()[0])
    a = np.delete(np.column_stack((a, np.array(ohe))), 0, 1)
    return(a)

def dta_target(a):
    a = np.array(a)
    tg = a[:, 7].reshape(-1, 1)
    a = np.delete(a, 7, 1)
    return(a, tg)

def prepare(dat):
    dat = np.delete(dat, 0)
    dat = dta_metro([dat])
    if dat[0][1] == "True":
        dat[0][1] = 1
    else: dat[0][1] = 0
    dat, tar = dta_target(dat)
    return(dat, tar)