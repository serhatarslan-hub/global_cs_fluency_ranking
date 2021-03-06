"""
This snippet has been prepared with the help provided at the following
blog entry:
https://www.analyticsvidhya.com/blog/2017/01/t-sne-implementation-r-python/
"""

import csv
import numpy as np
import matplotlib.pyplot as plt

from time import time
from matplotlib.cm import rainbow
from matplotlib import offsetbox
from sklearn import manifold
from adjustText import adjust_text


def plot_country_clustering(X, y, label, spacing, title=None):
    """
    Scales and plots the different countries' embeddings.
    """
    colormap = rainbow(np.linspace(0, 1, label.size))
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    plt.figure()
    texts = []
    for i in range(X.shape[0]):
        plt.plot(X[i, 0], X[i, 1], marker=".", c=colormap[label[i]-1])
        if i % spacing == 0:
            texts.append(plt.text(X[i, 0], X[i, 1], y[i], fontdict={'weight': 'bold', 'size': 9}))

    adjust_text(texts)
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)


def main(infile = 'GT_Analysis_All_Final.xlsx', verbose = False):
    """
    Parses the data from the infile, along with labels, and plots the t-SNE
    embedding.
    """

    country_list = []

    # Get country names separately since np parses them as nans
    with open(infile, 'r') as csvfile:
        country_dist = csv.reader(csvfile, delimiter=',')
        for row in country_dist:
            country_list.append(row[0])

    # TODO (@Mo): Labels below don't work properly. Need to update with Chris' code.
    country_dist = np.genfromtxt(infile, delimiter=",")
    X = country_dist[:, 1:]
    label = country_dist[:, 0]
    label = label.astype(np.int64)
    n_samples, n_features = X.shape
    n_neighbors = 10

    if args.verbose:
        print("Computing t-SNE embedding")

    tsne = manifold.TSNE(n_components=2, perplexity=n_neighbors,
                         init='pca', random_state=0)
    X_tsne = tsne.fit_transform(X)
    plot_country_clustering(X_tsne, country_list, label, 5,
            "Clustering for countries with %d keywords" % X.shape[1])
    plt.show()

if __name__ == '__main__':
    main()
