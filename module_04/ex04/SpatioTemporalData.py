from FileLoader import FileLoader
import pandas as pd


class SpatioTemporalData:
    def __init__(self,df):
        if not isinstance(df,pd.DataFrame):
            return None
        self.df=df
    def when(self,location):
        if not isinstance(location,str):
            return None
        df=self.df[self.df['City']==location]
        lst=[year for year in df['Year']]
        lst=list(set(lst))
        lst.sort()
        return lst
    def where(self,date):
        if not isinstance(date,int):
            return None
        df=self.df[self.df['Year']==date]
        lst=[]
        lst.append(df['City'].min())
        return lst

fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
std=SpatioTemporalData(df)
print(std.when('Paris'))
print(std.where(2012))