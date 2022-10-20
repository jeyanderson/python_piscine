from FileLoader import FileLoader
import pandas as pd

def proportion_by_sport(df,year,sport,gender):
    df=df[df['Year']==year]
    df = df.drop_duplicates(subset='ID', keep='first')
    gender_total=df[df['Sex']==gender]
    sport_total=gender_total[gender_total['Sport']==sport]
    return  sport_total.size/gender_total.size

fl=FileLoader()
df=fl.load('../resources/athlete_events.csv')
print(proportion_by_sport(df,2004,'Tennis','F'))