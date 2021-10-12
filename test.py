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

print(np.array(list(pars('https://www.domofond.ru/2-komnatnaya-kvartira-v-arendu-moskva-2425453201').values())))