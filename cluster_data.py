## importing the required packages
import csv
from time import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import rainbow
from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
             discriminant_analysis, random_projection)
"""
    This snippet has been prepared with the help provided at the following 
    blog entry: 
    https://www.analyticsvidhya.com/blog/2017/01/t-sne-implementation-r-python/
"""

## Function to Scale and visualize the embedding vectors
def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)     
    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.text(X[i, 0], X[i, 1], str(digits.target[i]),
                 color=plt.cm.Set1(y[i] / 10.),
                 fontdict={'weight': 'bold', 'size': 9})
    if hasattr(offsetbox, 'AnnotationBbox'):
        ## only print thumbnails with matplotlib > 1.0
        shown_images = np.array([[1., 1.]])  # just something big
        for i in range(digits.data.shape[0]):
            dist = np.sum((X[i] - shown_images) ** 2, 1)
            if np.min(dist) < 4e-3:
                ## don't show points that are too close
                continue
            shown_images = np.r_[shown_images, [X[i]]]
            imagebox = offsetbox.AnnotationBbox(
                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
                X[i])
            ax.add_artist(imagebox)
    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)

def plot_country_clustering(X,y,label,spacing,title=None):
    colormap = rainbow(np.linspace(0, 1, label.size))
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)     
    plt.figure()
    for i in range(X.shape[0]):
        plt.plot(X[i, 0], X[i, 1],marker=".",
                 c = colormap[label[i]-1])
        if i % spacing == 0:
            plt.text(X[i, 0], X[i, 1], y[i],
                 fontdict={'weight': 'bold', 'size': 9})
    if title is not None:
        plt.title(title)
    plt.xticks([]), plt.yticks([])
             
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
## Loading and curating the data
countryList = []
with open('./tmp/CountryDistKeywords.csv') as csvfile:
    countryDist = csv.reader(csvfile, delimiter=';')
    for row in countryDist:
        countryList.append(row[1])

countryDist = np.genfromtxt ('./tmp/CountryDistKeywords.csv', delimiter=";")
X = countryDist[:,2:]
label = countryDist[:,0]
label = label.astype(np.int64)
n_samples, n_features = X.shape
n_neighbors = 10

## Computing t-SNE
print("Computing t-SNE embedding")
tsne = manifold.TSNE(n_components=2, perplexity=n_neighbors,
                     init='pca', random_state=0)
X_tsne = tsne.fit_transform(X)

plot_country_clustering(X_tsne, countryList, label, 5,
        "Clustering for countries with %d keywords"%X.shape[1])
plt.show()
