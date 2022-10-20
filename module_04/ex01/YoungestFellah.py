import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df,year):
    if not isinstance(df,pd.DataFrame) or not isinstance(year,int):
        return None
    yearly_df=df[df['Year']==year]
    dct={}
    dct['f']=yearly_df[yearly_df['Sex']=='F']['Age'].min()
    dct['h']=yearly_df[yearly_df['Sex']=='M']['Age'].min()
    return dct

fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
print(youngest_fellah(df,2012))