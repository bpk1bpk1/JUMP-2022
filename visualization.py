import potential_portfolios
import matplotlib.pyplot as plt
import pandas as pd

class PortfolioGraph:
    def __init__(self):
        self.client = potential_portfolios.client


data = pd.read_csv("Visualization.csv", index_col=False)
data["period"] = data["YEAR"].astype(str) + data["QUARTER"]
user_portfolio = ["BF", "AF", "BE", "AI", "M"]
potential_portfolio = ["BF", "AF", "BJ", "AL", "AY"]


# Original Portfolio
op_data = data.TICKER.isin(user_portfolio)
op = data[op_data]
# Points by portfolio
op_agg1 = op.groupby('period').agg({'MONEY': 'mean'}).reset_index()
op_agg2 = op.groupby('period').agg({'CARBON_FOOTPRINT': 'mean'}).reset_index()

# Potential Portfolio
pp_data = data.TICKER.isin(potential_portfolio)
pp = data[pp_data]
pp_agg1 = pp.groupby('period').agg({'MONEY': 'mean'}).reset_index()
pp_agg2 = pp.groupby('period').agg({'CARBON_FOOTPRINT': 'mean'}).reset_index()

# create figure and axis objects with subplots
fig, ax = plt.subplots()
ax2 = ax.twinx()

# Original Plot
plt.plot(op_agg2.period, op_agg2.CARBON_FOOTPRINT, marker="o", label="Current Carbon Footprint")
plt.plot(op_agg1.period, op_agg1.MONEY, marker="o", label="Current Returns")

# Potential Portfolio Plot
plt.plot(pp_agg2.period, pp_agg2.CARBON_FOOTPRINT, linestyle='dashed', marker="o", label="Potential Carbon Footprint")
plt.plot(pp_agg1.period, pp_agg1.MONEY, linestyle='dashed', marker="o", label="Potential Returns")

# Labelling
ax.set_xlabel("Time Periods", fontsize=14)
ax.set_ylabel("Carbon Footprint(tCO\u2082e/bnUSD)", color="red", fontsize=14)
ax2.set_ylabel("Returns", color="blue", fontsize=14)

ax.legend()
plt.legend()
plt.show()
