from FileLoader import FileLoader

def howManyMedalsByCountry(df, country):
    dic = {}
    data = df[df.Team == country]
    for year in data['Year'].drop_duplicates():
        dic[year] = {}
        medal_tab_per_year = data[data.Year == year].drop_duplicates('Event').groupby('Medal').count()
        for rank, row in medal_tab_per_year.iterrows():
            dic[year][rank] = row['ID']
    return dic


if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(howManyMedalsByCountry(dataframe, 'France'))
