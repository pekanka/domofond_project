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
import catboost

def pr_price(dat):
    with open("pr_selector.pkl", "rb") as f:
        slc = cPickle.load(f)
    price_t = slc.predict([dat[0]])[0]
    if price_t == 0:
        with open("cheap_apart_pred.pkl", "rb") as f:
            model = cPickle.load(f)
    else:
        with open("exp_apart_pred.pkl", "rb") as f:
            model = cPickle.load(f)
    predicted_pr = model.predict([dat[0]])
    return(predicted_pr)