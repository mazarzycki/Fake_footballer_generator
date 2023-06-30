import datetime
import pandas as pd
import random
from data import ENG, ITA, SPA, BRA, position

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

        return {
            'first_name': first_name,
            'last_name': last_name,
            'position': position,
            'nationality': nationality,
            'club': club,
            'dob': date_of_birth
        }

# Set the country code manually
country = 'ENG'

footballer_generator = FootballerGenerator(ENG[0], ENG[1], ENG[2], ENG[3], position)

# Set the number of fake footballers to generate manually
num_footballers = 10

# Generate fake footballers
fake_footballers = [footballer_generator.generate_fake_footballer(country) for _ in range(num_footballers)]

# Create DataFrame from the list of footballers
df = pd.DataFrame(fake_footballers)

# Save DataFrame to Excel file
filename = f'fake_{country}_footballers.xlsx'
df.to_excel(filename, index=False)
print(f"Fake footballers data saved to {filename}:\n")
print(df)
