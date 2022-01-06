import pandas as pd
import random
import numpy as np

Climate_Change = []
Governance = []
People = []
Pollution_Waste = []
Products_Services = []
Water = []
Sustainability_Rating = []
Carbon_Footprint = []
WACI = []

df = pd.DataFrame()

for i in range(0, 67):
    Climate_Change.append(round(random.uniform(0, 9), 3))

for i in range(0, 67):
    Governance.append(round(random.uniform(1, 9.5), 3))

for i in range(0, 67):
    People.append(round(random.uniform(0, 7.7), 3))

for i in range(0, 67):
    Pollution_Waste.append(round(random.uniform(0, 8.5), 3))

for i in range(0, 67):
    Products_Services.append(round(random.uniform(0, 6.9), 3))

for i in range(0, 67):
    Water.append(round(random.uniform(1, 8.8), 3))

for i in range(0, 67):
    Sustainability_Rating.append(round(random.uniform(0.7, 8.8), 3))

for i in range(0, 67):
    Carbon_Footprint.append(round(random.uniform(1.5, 240.07), 3))

for i in range(0, 67):
    WACI.append(round(random.uniform(3.5, 723), 3))

df['Climate_Change'] = Climate_Change
df['Governance'] = Governance
df['People'] = People
df['Pollution_Waste'] = Pollution_Waste
df['Products_Services'] = Products_Services
df['Water'] = Water
df['Sustainability_Rating'] = sorted(Sustainability_Rating, reverse=True)
df['Carbon_Footprint'] = sorted(Carbon_Footprint)
df['WACI'] = sorted(WACI)


df.to_csv('Data_populated_sorted.csv', sep=",", header=True, index=False)

df = pd.read_csv("Data_populated.csv", index_col=False)
df['TICKER'] = np.random.permutation(df['TICKER'].values)

df.to_csv('Data_populated_TICKERS.csv', sep=",", header=True, index=False)