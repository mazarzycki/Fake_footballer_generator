import datetime
import pandas as pd
import random
from data import ENG, ITA, SPA, GER, position

class FootballerGenerator:
    def __init__(self, first_names, last_names, cities, club, position):
        self.first_names = first_names
        self.last_names = last_names
        self.cities = cities
        self.club = club
        self.position = position
        
    @staticmethod
    def generate_random_date_of_birth(start_year, end_year):
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 12, 31)
        random_date = start_date + datetime.timedelta(days=random.randint(0, (end_date - start_date).days))
        return random_date

    def generate_fake_footballer(self, nationality):
        first_name = random.choice(self.first_names)
        last_name = random.choice(self.last_names)
        club = random.choice(self.cities) + ' ' + random.choice(self.club)
        position = random.choice(self.position)
        date_of_birth = self.generate_random_date_of_birth(1986, 2005)
        matches_played = random.randint(1, 34)
        minutes_played = random.randint(matches_played, matches_played * 90)
        # TODO Make goals and assists more realistic
        # TODO Add more statistics: xG and others
        goals = (lambda pos: 0 if pos == "GK" else random.randint(0, min(minutes_played // 50, 6)) if pos in ["LB", "CB", "RB"] else random.randint(0, min(minutes_played // 50, 9)) if pos in ["DM", "CM"] else random.randint(0, min(minutes_played // 50, 12)) if pos in ["AM", "LM", "RM"] else random.randint(0, min(minutes_played // 30, 28)))(position)
        assists = (lambda pos: random.randint(0, min(minutes_played // 50, 3)) if pos == "GK" else random.randint(0, min(minutes_played // 50, 6)) if pos in ["LB", "CB", "RB"] else random.randint(0, min(minutes_played // 50, 9)) if pos in ["DM", "CM"] else random.randint(0, min(minutes_played // 50, 12)) if pos in ["AM", "LM", "RM"] else random.randint(0, min(minutes_played // 50, 19)))(position)


        return {
            'first_name': first_name,
            'last_name': last_name,
            'position': position,
            'nationality': nationality,
            'club': club,
            'dob': date_of_birth, 
            'matches_played': matches_played,
            'minutes_played': minutes_played,
            'goals': goals,
            'assists': assists
        }

# Map the user's choice to the country code
country_mapping = {
    '1': 'ENG',
    '2': 'ITA',
    '3': 'SPA',
    '4': 'GER'
}

datasets = []  # List to store generated datasets

while True:
    print("Available countries:")
    print("1. England (ENG)")
    print("2. Italy (ITA)")
    print("3. Spain (SPA)")
    print("4. Germany (GER)")

    country_choice = input("Enter the number corresponding to the desired country.\nLater you will be asked the same question once again if you want to create a data set with players from different countries (or 'q' to quit): ")

    if country_choice.lower() == 'q':
        break  # Exit the loop if user enters 'q'

    # Validate the user's choice
    if country_choice not in country_mapping:
        print("Invalid country choice. Please try again.")
        continue  # Continue to the next iteration of the loop

    country = country_mapping[country_choice]

    # Set up the FootballerGenerator based on the chosen country
    if country == 'ENG':
        footballer_generator = FootballerGenerator(ENG[0], ENG[1], ENG[2], ENG[3], position)
    elif country == 'ITA':
        footballer_generator = FootballerGenerator(ITA[0], ITA[1], ITA[2], ITA[3], position)
    elif country == 'SPA':
        footballer_generator = FootballerGenerator(SPA[0], SPA[1], SPA[2], SPA[3], position)
    elif country == 'GER':
        footballer_generator = FootballerGenerator(GER[0], GER[1], GER[2], GER[3], position)

    # Prompt the user to enter the number of fake footballers to generate
    num_footballers = input("Enter the number of fake footballers to generate: ")

    # Validate the user's input for the number of footballers
    if not num_footballers.isdigit() or int(num_footballers) <= 0:
        print("Invalid number of footballers. Please try again.")
        continue  # Continue to the next iteration of the loop

    num_footballers = int(num_footballers)

    # Generate fake footballers
    fake_footballers = [footballer_generator.generate_fake_footballer(country) for _ in range(num_footballers)]

    datasets.append(pd.DataFrame(fake_footballers))  # Add the generated dataset to the list

# Concatenate and save all datasets to a single Excel file
filename = 'fake_footballers.xlsx'
final_dataset = pd.concat(datasets)
final_dataset.to_excel(filename, index=False)
print(f"Fake footballers data saved to {filename}:\n")
print(final_dataset)