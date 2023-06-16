import pandas as pd

class FileLoader:
    def load(self, path):
        if not isinstance(path, str):
            print("Path must be a string")
            return None
        try:
            df = pd.read_csv(path)
            print("Loading dataset of dimensions {} x {}".format(df.shape[0], df.shape[1]))
            return df
        except Exception as e:
            if isinstance(e, FileNotFoundError):
                print("File not found")
            else:
                print("Error while loading file")
            return None
        
    def display(self, df, n):
        if not isinstance(n, int):
            print("n must be an integer")
            return None
        if df is None:
            print("No data to be displayed")
            return None
        if n > 0:
            print(df.head(n))
        else:
            print(df.tail(-n))
            
if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")
    loader.display(data, 12)
    loader.display(data, -12)