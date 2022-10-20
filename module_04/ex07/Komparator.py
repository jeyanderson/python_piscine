import pandas as pd
from FileLoader import FileLoader
from pandas.api.types import is_numeric_dtype
import matplotlib.pyplot as plt
import seaborn as sns

class Komparator:
    def __init__(self,df):
        if not isinstance(df,pd.DataFrame):
            return None
        self.df=df
    def compare_box_plots(self,categorical_var,numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print('column not found.')
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('not a numerical variable.')
            return None
        sns.boxplot(x=self.df[categorical_var],y=self.df[numerical_var])
        plt.show()
    def density(self,categorical_var,numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print('column not found.')
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('not a numerical variable.')
            return None
        sns.kdeplot(data=self.df,x=numerical_var,hue=categorical_var)
        plt.show()
    def compare_histograms(self,categorical_var,numerical_var):
        if categorical_var not in self.df or numerical_var not in self.df:
            print('column not found.')
            return None
        if not is_numeric_dtype(self.df[numerical_var]):
            print('not a numerical variable.')
            return None
        sns.histplot(data=self.df,x=numerical_var,hue=categorical_var)
        plt.show()
    

fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
kmp=Komparator(df)
kmp.compare_histograms('Medal','Age')