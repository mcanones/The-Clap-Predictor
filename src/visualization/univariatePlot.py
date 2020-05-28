import pandas as pd 
import matplotlib.pyplot as plt  

def plot_univariate(data_concat, X, y, figsize=(12, 8)):
    y_right_label = f'mean for target column: {y}'
    y_left_label = 'number of observations'
    #bar plot of y count
    ax_X = data_concat[y,'count'].plot(kind='bar',legend=True,label=y_left_label,color='#84c2bd',figsize=figsize)
    ax_X.set_ylabel(y_left_label)
    ax_X.set_xlabel(X)
    #normal plot y mean
    ax_y = data_concat[y,'mean'].plot(legend=True, secondary_y=True, title=f'Univariate plot for feature: {X}', label=y_right_label, marker='o', color='#c40222', xlim=ax_X.get_xlim(), rot=90 if len(data_concat.index) > 10 else 0)
    ax_y.set_ylabel(y_right_label)
    plt.savefig(f'../reports/figures/Univariate{X} .png', bbox_inches = 'tight')
    plt.show()
    
def plot_univariate_numerical(data, X, y, minimum=None, maximum=None, bins=10):
    if minimum and not maximum:
        clipped_col = data[X].clip(lower=minimum)
    elif not minimum and maximum:
        clipped_col = data[X].clip(upper=maximum)
    elif minimum and maximum:
        clipped_col = data[X].clip(minimum, maximum)
    else:
        clipped_col = data[X]
    #cut classify each serie value in an interval
    #I have lots of values repeated (few numbers fall under the same interval)
    #We count number of claps and calculate mean for each interval 
    data_concat = pd.concat([pd.cut(clipped_col, bins), data[y]], axis=1).groupby(X).agg({y: ['mean', 'count']})
    plot_univariate(data_concat, X, y)
    #return data_concat
    
def plot_univariate_ordinal(data, X, y):
    data_concat = pd.concat([data[X], data[y]], axis=1).groupby(X).agg({y: ['mean', 'count']})
    plot_univariate(data_concat, X, y)
    #return data_concat

def plot_univariate_categorical(data, X, y):
    df_groupby = data.groupby(X).agg({y: ['mean', 'count']})
    df_groupby = df_groupby.sort_values((y, 'mean'), ascending=False)
    plot_univariate(df_groupby, X, y)
    #return df_groupby
