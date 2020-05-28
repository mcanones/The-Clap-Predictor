import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def distPlot(data, cols):

    f, axes = plt.subplots(len(cols), 1, figsize=[20,20])

    for i in range(len(cols)):
        sns.distplot(data[cols[i]], ax=axes[i], bins=200, kde=False)

    f.savefig('../reports/figures/Histograms.png')
    plt.show()


"""
def distPlot(data, cols_d, cols_c):

    f, axes = plt.subplots(len(cols_d+cols_c), 1, figsize=[20,15])

    #discrete
    for i in range(len(cols_d)):
        sns.distplot(data[cols_d[i]],  ax=axes[i], bins=50, kde_kws={'bw':1})

    #continuous
    for i in range(len(cols_c)):
        sns.distplot(data[cols_c[i]], ax=axes[len(cols_d)+i], bins=200)

    f.savefig('../reports/figures/Histograms.png')
    plt.show()
"""
