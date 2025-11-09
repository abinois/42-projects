import pandas as pd

class FileLoader():

    def load(self, path):
        try:
            df = pd.read_csv(path)
            print('Loading dataset of dimensions {} x {}'.format(df.shape[0], df.shape[1]))
        except:
            exit('Error loading file.')
        return df

    def display(self, df, n):
        if type(df) is pd.DataFrame and n != 0:
         print((df.tail(-n), df.head(n))[n > 0])
        else:
            exit('Wrong parameters.')


if __name__ == '__main__':
    fl = FileLoader()
    dataframe = fl.load('athlete_events.csv')
    fl.display(dataframe, 5)
    fl.display(dataframe, -5)
