from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df
    
    def when(self, location):
        return self.df[self.df['City'] == location]['Year'].drop_duplicates().to_list()
    
    def where(self, date):
        return self.df[self.df['Year'] == date]['City'].drop_duplicates().to_list()
        
if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ex01/data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
    print(sp.when('Seoul'))