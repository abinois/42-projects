
import pandas as pd
from FileLoader import FileLoader

def YoungestFellah(df, year):
    if type(df) is not pd.DataFrame or type(year) is not int or year < 1:
        exit('Wrong parameters.')
    sub_data = df[df.Year == year].sort_values('Age')
    if sub_data.empty:
        exit('Not an Olympic year.')
    dudes = sub_data[sub_data.Sex == 'M'].reset_index()
    chicks = sub_data[sub_data.Sex == 'F'].reset_index()
    dic = {
        dudes.loc[0, 'Sex']: dudes.loc[0, 'Age'],
        chicks.loc[0, 'Sex']: chicks.loc[0, 'Age']}
    return dic

if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(YoungestFellah(dataframe, 2004))
    print(YoungestFellah(dataframe, 2003))

