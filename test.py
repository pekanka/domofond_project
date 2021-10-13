import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import metrics
from sklearn import cluster
from html_parser import pars
import data_prep
from pr_destribute import pr_dest
import _pickle as cPickle
import pred

data = np.array(list(pars('https://www.domofond.ru/2-komnatnaya-kvartira-v-arendu-moskva-1654620527').values()))
with open("pr_selector.pkl", "rb") as f:
    slc = cPickle.load(f)
data = data_prep.prepare(data)[0].astype(float)
print(pred.pr_price(data))
