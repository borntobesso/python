from FileLoader import FileLoader

def proportion_by_sport(df, year, sport, sex):
    # Filter the dataset for the given year and sex
	year_df = df[df['Year'] == year]
	sex_df = year_df[year_df['Sex'] == sex]
	
	# Drop duplicated individuals to count only unique ones
	unique_individuals = sex_df.drop_duplicates(subset='ID')
	if len(unique_individuals) == 0:
		return None
	
	# Calculate the proportion of the participants who played the given sport among the participants of the given gender
	sport_df = unique_individuals[unique_individuals['Sport'] == sport]
	proportion = len(sport_df) / len(unique_individuals)
	return proportion

if __name__ == "__main__":
	loader = FileLoader()
	data = loader.load('../ex01/data/athlete_events.csv')
	print(proportion_by_sport(data, 2004, 'Tennis', 'F'))
	print(proportion_by_sport(data, 2004, 'Tennis', 'M'))
	print(proportion_by_sport(data, 2004, 'Basketball', 'F'))
	print(proportion_by_sport(data, 2004, 'Basketball', 'M'))
	print(proportion_by_sport(data, 2000, 'Swimming', 'F'))
	print(proportion_by_sport(data, 2000, 'Swimming', 'M'))
	print(proportion_by_sport(data, 1948, 'Gymnastics', 'F'))
	print(proportion_by_sport(data, 1948, 'Gymnastics', 'M'))