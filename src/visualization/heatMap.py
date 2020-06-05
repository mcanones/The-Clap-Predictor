
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def heatMap(data):
    corr = data.corr()
    f, ax = plt.subplots(figsize=(20, 20))
    cmap = sns.diverging_palette(220, 10, as_cmap=True)
    sns.heatmap(corr, cmap=cmap, vmax=1, center=0, square=True, linewidths=0.2, cbar_kws={"shrink": 0.5})
    f.savefig('../reports/figures/HeatMap.png')
    plt.show()
    
