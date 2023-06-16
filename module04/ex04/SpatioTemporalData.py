from FileLoader import FileLoader

class SpatioTemporalData:
    def __init__(self, df):
        self.df = df
    
    def when(self, location):
        return self.df[self.df['City'] == location]['Year'].drop_duplicates().to_list()
    
    def where(self, date):
        return self.df[self.df['Year'] == date]['City'].drop_duplicates().to_list()