import seaborn as sns
import matplotlib.pyplot as plt

def boxPlot(df, cols, figsize):
    f, axes = plt.subplots(len(cols), 1, figsize=figsize)
    for i,col in enumerate(cols):
        sns.boxplot(y=col, data=df,  orient='h' , ax=axes[i])
    f.savefig('../reports/figures/BoxPlot.png')
    plt.show()
