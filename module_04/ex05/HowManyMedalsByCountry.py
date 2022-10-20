from FileLoader import FileLoader
import pandas as pd
import numpy as np

def how_many_medals_by_country(df,country_name):
    if not isinstance(df,pd.DataFrame) or not isinstance(country_name,str):
        return None
    dct={}
    df=df[df['Team']==country_name]
    df=df.replace({'Medal':{'Gold':'G','Silver':'S','Bronze':'B'}})
    team_sports = ['Basketball','Football', 'Tug-Of-War','Badminton','Sailing','Handball','Water Polo','Hockey','Rowing','Bobsleigh','Softball','Volleyball','Synchronized Swimming','Baseball','Rugby Sevens','Rugby','Lacrosse','Polo']
    team_df=df[df['Sport'].isin(team_sports)]
    team_df=team_df.drop_duplicates(subset=['Games','Event','Medal'])
    ind_df=df[~df['Sport'].isin(team_sports)]
    df=pd.concat([ind_df,team_df])
    df=df.groupby(['Year','Medal'],dropna=False).size()
    df=df.unstack(fill_value=0)
    if np.nan in df:
        df=df.drop(np.nan,axis=1)
    dct=df.to_dict(orient='index')
    return dct


fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
print(how_many_medals_by_country(df,'France'))