import pandas as pd
import random

CarbonFootprint_Q1_2019 = []
CarbonFootprint_Q2_2019 = []
CarbonFootprint_Q3_2019 = []
CarbonFootprint_Q4_2019 = []

CarbonFootprint_Q1_2020 = []
CarbonFootprint_Q2_2020 = []
CarbonFootprint_Q3_2020 = []
CarbonFootprint_Q4_2020 = []

CarbonFootprint_Q1_2021 = []
CarbonFootprint_Q2_2021 = []
CarbonFootprint_Q3_2021 = []
CarbonFootprint_Q4_2021 = []
YEAR = []
QUARTER = []

df = pd.DataFrame()

years = [2019, 2020, 2021]
# 2019
for i in range(0, 67):
    CarbonFootprint_Q3_2021.append(round(random.uniform(2.7, 250.07), 3))

df['CarbonFootprint_Q3_2021'] = sorted(CarbonFootprint_Q3_2021)
print(df['CarbonFootprint_Q3_2021'])
df.to_csv('TRIAL.csv', sep=",", header=True, index=False)


# for i in range(0, 67):
#     CarbonFootprint_Q2_2019.append(round(random.uniform(6.3, 300.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q3_2019.append(round(random.uniform(6.1, 300.07), 3))

# for i in range(0, 67):
#     CarbonFootprint_Q4_2019.append(round(random.uniform(5.8, 300.07), 3))
#
# # 2020
# for i in range(0, 67):
#     CarbonFootprint_Q1_2020.append(round(random.uniform(4.9, 295.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q2_2020.append(round(random.uniform(4.8, 290.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q3_2020.append(round(random.uniform(4.4, 285.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q4_2020.append(round(random.uniform(4.2, 280.07), 3))
#
# # 2021
# for i in range(0, 67):
#     CarbonFootprint_Q1_2021.append(round(random.uniform(3.6, 275.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q2_2021.append(round(random.uniform(3.2, 270.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q3_2021.append(round(random.uniform(2.7, 250.07), 3))
#
# for i in range(0, 67):
#     CarbonFootprint_Q4_2021.append(round(random.uniform(1.5, 240.07), 3))


# df['CarbonFootprint_Q1_2019'] = sorted(CarbonFootprint_Q1_2019, reverse=True)
# df['CarbonFootprint_Q2_2019'] = sorted(CarbonFootprint_Q2_2019, reverse=True)
# df['CarbonFootprint_Q3_2019'] = sorted(CarbonFootprint_Q3_2019, reverse=True)
# df['CarbonFootprint_Q4_2019'] = sorted(CarbonFootprint_Q4_2019, reverse=True)
#
# df['CarbonFootprint_Q1_2020'] = sorted(CarbonFootprint_Q1_2020, reverse=True)
# df['CarbonFootprint_Q2_2020'] = sorted(CarbonFootprint_Q2_2020, reverse=True)
# df['CarbonFootprint_Q3_2020'] = sorted(CarbonFootprint_Q3_2020, reverse=True)
# df['CarbonFootprint_Q4_2020'] = sorted(CarbonFootprint_Q4_2020, reverse=True)
#
# df['CarbonFootprint_Q1_2021'] = sorted(CarbonFootprint_Q1_2021, reverse=True)
# df['CarbonFootprint_Q2_2021'] = sorted(CarbonFootprint_Q2_2021, reverse=True)
# df['CarbonFootprint_Q3_2021'] = sorted(CarbonFootprint_Q3_2021, reverse=True)
# df['CarbonFootprint_Q4_2021'] = sorted(CarbonFootprint_Q4_2021, reverse=True)
#
# df.to_csv('QUARTER_CARBON_TICKERS.csv', sep=",", header=True, index=False)