from FileLoader import FileLoader

class SpatioTemporalData():
    def __init__(self, df):
        self.data = df

    def where(self, year):
        filter = self.data[self.data.Year == year].iloc[0, 11]
        return [filter]

    def when(self, location):
        filter = list(self.data[self.data.City == location].loc[:, 'Year'].drop_duplicates())
        return filter


if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('../ex00/athlete_events.csv')
    sp = SpatioTemporalData(dataframe)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))