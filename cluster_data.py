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

"""
## Loading and curating the data
digits = datasets.load_digits(n_class=10)
X = digits.data
y = digits.target
n_samples, n_features = X.shape
n_neighbors = 30
## Computing t-SNE
print("Computing t-SNE embedding")
tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
t0 = time()
X_tsne = tsne.fit_transform(X)
plot_embedding(X_tsne,
               "t-SNE embedding of the digits (time %.2fs)" %
               (time() - t0))
plt.show()
"""

def plot_embedding(X, title=None):
    """
    Scales and plots the given embedding vectors (X), along with annotations for
    every point.
    """

    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    plt.figure()
    ax = plt.subplot(111) # top-left subplot in a grid of 1x1 subplots
    for i in range(X.shape[0]):
        plt.text(
            X[i, 0],
            X[i, 1],
            str(digits.target[i]),
            color=plt.cm.Set1(y[i] / 10.),
            fontdict={'weight': 'bold', 'size': 9},
            )

    if hasattr(offsetbox, 'AnnotationBbox'):
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, axis = 1)
            if np.min(dist) < 4e-3:
                # Don't plot points that are too close
                continue

            shown_images = np.r_[shown_images, [X[i]]] # Concatenation
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(
                    digits.images[i],
                    cmap=plt.cm.gray_r),
                X[i],
                )
            ax.add_artist(imagebox)

    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)

def plot_country_clustering(X, y, label, spacing, title=None):
    """
    Scales and plots the different countries' embeddings.
    """
    colormap = rainbow(np.linspace(0, 1, label.size))
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)
    plt.figure()
    for i in range(X.shape[0]):
        plt.plot(X[i, 0], X[i, 1], marker=".", c=colormap[label[i]-1])
        if i % spacing == 0:
            plt.text(X[i, 0], X[i, 1], y[i], fontdict={'weight': 'bold', 'size': 9})

    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)


def main(infile = './tmp/CountryDistKeywords.csv', verbose = False):
    """
    Parses the data from the infile, along with labels, and plots the t-SNE
    embedding.
    """
    
    country_list = []

    # TODO (@Mo): Can't this be combined with np.genfromtxt below?
    with open(infile) as csvfile:
        country_dist = csv.reader(csvfile, delimiter=';')
        for row in countryDist:
            country_list.append(row[1])

    country_dist = np.genfromtxt(infile, delimiter=";")
    X = country_dist[:, 2:]
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
            "Clustering for countries with %d keywords"%X.shape[1])
    plt.show()

if __name__ == '__main__':
    main()
