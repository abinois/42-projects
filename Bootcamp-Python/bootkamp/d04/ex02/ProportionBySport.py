from FileLoader import FileLoader

def proportionBySport(df, year, sport, gender):
    sub_data = df[(df.Year == year) & (df.Sex == gender)].drop_duplicates('Name')
    total = sub_data.shape[0]
    sport_slice = sub_data[sub_data.Sport == sport].shape[0]
    res = sport_slice * 100 / total
    string = 'The propotion of {} that played {} in {} is {}.'.format(('men', 'women')[gender == 'F'], sport, year, res)
    return string


if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    print(proportionBySport(dataframe, 2004, 'Tennis', 'F'))