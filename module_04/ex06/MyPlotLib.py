import pandas as pd
from FileLoader import FileLoader
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns

class MyPlotLib:
    def __init__(self):
        pass
    @staticmethod
    def histogram(data,features):
        if not isinstance(data,pd.DataFrame) or not isinstance(features,list):
            return None
        features=list(filter(lambda x: is_numeric_dtype(data[x]),features))
        data[features].hist()
        plt.show()
    @staticmethod
    def density(data,features):
        if not isinstance(data,pd.DataFrame) or not isinstance(features,list):
            return None
        data[features].plot.kde()
        plt.show()
    @staticmethod
    def pair_plot(data,features):
        if not isinstance(data,pd.DataFrame) or not isinstance(features,list):
            return None
        sns.pairplot(data[features],diag_kind='hist',diag_kws=dict(bins=10),plot_kws=dict(s=7))
        plt.show()
    @staticmethod
    def box_plot(data,features):
        if not isinstance(data,pd.DataFrame) or not isinstance(features,list):
            return None
        features=list(filter(lambda x: is_numeric_dtype(data[x]),features))
        data.boxplot(column=features)
        plt.show()

fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
mpl=MyPlotLib()
mpl.histogram(df,['Height','Weight'])
mpl.density(df,['Height','Weight'])
mpl.pair_plot(df,['Height','Weight'])
mpl.box_plot(df,['Height','Weight'])