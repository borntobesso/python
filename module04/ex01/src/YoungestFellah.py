import pandas as pd
from FileLoader import FileLoader

def youngest_fellah(df, year):
    if not isinstance(df, pd.DataFrame):
        print("The first argument must be a pandas.DataFrame")
        return None
    if not isinstance(year, int):
        print("The second argument must be an integer")
        return None
    # Filter the dataset for the given year
    year_data = df[df['Year'] == year]
    
    # Filter the dataset for females and males separately
    females = year_data[year_data['Sex'] == 'F']
    males = year_data[year_data['Sex'] == 'M']
    
    # Find the minimum age for females and males
    youngest_female_age = females['Age'].min()
    youngest_male_age = males['Age'].min()
    
    # Create and return the dictionary with the youngest ages
    youngest_fellah_dict = {
        'Youngest Female Age' : youngest_female_age,
        'Youngest Male Age' : youngest_male_age
    }
    return youngest_fellah_dict
    
if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load("../data/athlete_events.csv")
    print(youngest_fellah(data, 2004))
    print(youngest_fellah(data, 1976))
    print(youngest_fellah(data, 1912))
    print(youngest_fellah(data,'2004'))