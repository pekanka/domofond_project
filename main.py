import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import linear_model
from sklearn import model_selection
from sklearn import preprocessing
from sklearn import metrics
from sklearn import cluster
from scripts.html_parser import pars
from scripts import data_prep
from scripts.pr_destribute import pr_dest
import _pickle as cPickle
from scripts import pred
import typer

app = typer.Typer()

@app.command()
def main(link: str):
    data = np.array(list(pars(link).values()))
    with open("models/pr_selector.pkl", "rb") as f:
        slc = cPickle.load(f)
    data, tar = data_prep.prepare(data)
    data = data.astype(float)
    typer.echo("Predicted price:" + str(pred.pr_price(data)[0]))
    typer.echo("Real price:" + str(tar[0][0]))

if __name__ == "__main__":
    app()