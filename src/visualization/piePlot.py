import matplotlib.pyplot as plt
import pandas as pd

def piePlot(data, col):
    vals = data[f'{col}'].value_counts()
    f,ax = plt.subplots(figsize=(5,5))
    ax.pie(vals,  pctdistance=1.2)
    ax.legend(labels=vals.keys(),loc=1)
    f.savefig(f'../reports/figures/PiePlot{col}.png')
    plt.show()
