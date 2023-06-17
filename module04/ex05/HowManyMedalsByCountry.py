from FileLoader import FileLoader
import pandas as pd

def how_many_medals_by_country(df, country):
    if not isinstance(df, pd.DataFrame):
        return "ERROR: df is not a pandas.DataFrame"
    if not isinstance(country, str):
        return "ERROR: country is not a string"
    team_sports = ['Basketball', 'Football', 'Tug-Of-War', 'Badmin', 'Handball', 'Water Polo', 'Hockey', 'Rowing', 'Boxing', 'Volleyball', 'Synchronized Swimming', 'Baseball', 'Rugby', 'Lacrosse', 'Polo']
    
    country_df = df[df["Team"] == country]
    medals  = {}
    
    medal_mapping = {'Gold': 'G', 'Silver': 'S', 'Bronze': 'B'}
    
    for _, row in country_df.iterrows():
        year = row['Year']
        sport = row['Sport']
        medal_type = row['Medal']
        
        if year not in medals:
            medals[year] = {'G': 0, 'S': 0, 'B': 0}
        if medal_type in medal_mapping:
            if sport in team_sports:
                if medals[year][medal_mapping[medal_type]] == 0:
                    medals[year][medal_mapping[medal_type]] = 1
            else:
                medals[year][medal_mapping[medal_type]] += 1
            
    return medals

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ex01/data/athlete_events.csv')
    print(how_many_medals_by_country(data, 'France'))
    print(how_many_medals_by_country(data, 'Romania'))
    print(how_many_medals_by_country(data, 'Italy'))
    print(how_many_medals_by_country(data, 'Germany'))
    print(how_many_medals_by_country(data, 'South Korea'))