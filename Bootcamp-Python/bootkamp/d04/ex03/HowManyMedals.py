from FileLoader import FileLoader

def howManyMedals(df, name):
    sub_data = df[df.Name == name].groupby('Medal').count()
    if sub_data.empty:
        exit('Inconnu au bataillzer.')
    dic = {}
    for i in range(3):
        dic[sub_data.index[i]] = sub_data.iloc[i, 0]
    return dic

if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(howManyMedals(dataframe, 'Kjetil Andr Aamodt'))
    print(howManyMedals(dataframe, 'Serge Lama'))
