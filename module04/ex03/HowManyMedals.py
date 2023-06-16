from FileLoader import FileLoader

def how_many_medals(df, name):
    participant_data = df[df['Name'] == name]
    medals_dict = {}
    
    for _, row in participant_data.iterrows():
        year = row['Year']
        medal = row['Medal']
        
        if year not in medals_dict:
            medals_dict[year] = {'G': 0, 'S': 0, 'B': 0}
        if medal == 'Gold':
            medals_dict[year]['G'] += 1
        elif medal == 'Silver':
            medals_dict[year]['S'] += 1
        elif medal == 'Bronze':
            medals_dict[year]['B'] += 1
    return medals_dict

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ex01/data/athlete_events.csv')
    print(how_many_medals(data, 'Kjetil Andr Aamodt'))
    print(how_many_medals(data, 'Arvo Ossian Aaltonen'))
    print(how_many_medals(data, 'Tamila Rashidovna Abasova'))
    print(how_many_medals(data, 'Jang Mi-Ran'))
    