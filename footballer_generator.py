import pandas as pd
from data import ENG, ITA, SPA, BRA, position
from main import FootballerGenerator

country = 'ENG'  # Specify the desired country code

footballer_generator = FootballerGenerator(ENG[0], ENG[1], ENG[2], ENG[3], position)

num_footballers = 10  # Specify the number of fake footballers to generate

fake_footballers = [footballer_generator.generate_fake_footballer(country) for _ in range(num_footballers)]

df = pd.DataFrame(fake_footballers)

filename = f'fake_{country}_footballers.xlsx'
df.to_excel(filename, index=False)
print(f"Fake footballers data saved to {filename}:\n")
print(df)
