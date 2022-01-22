import math
import pandas as pd
import itertools
import matplotlib.pyplot as plt


class Recommend_Carbon_Portfolio:
    def __init__(self):
        self.expected_normalized_score = None
        self.expected_sustainability_rating = None
        self.expected_carbon_footprint = None
        self.potential_portfolio = []
        self.current_normalized_score = None
        self.potential_df = None
        self.percent_of_change = int(input("Enter the percentage of change to the portfolio: "))
        self.current_sustainability_rating = None
        self.current_carbon_footprint = None
        self.df = pd.read_csv("Data.csv", index_col=False)
        self.portfolio_user_1 = ["BF", "AF", "BE", "AI", "M"]  # Portfolio Tickers

    # Subset of df
    def filter_rows_by_values(self, df, col, values):
        return df[~df[col].isin(values)]

    # Normalize Carbon Score
    def normalize_carbon_score(self, score):
        max_value = self.df['Carbon_Footprint'].max() / len(self.portfolio_user_1)
        min_value = self.df['Carbon_Footprint'].min() / len(self.portfolio_user_1)
        return round(10 - (score - min_value) / (max_value - min_value), 2)

    # Current Sustainability Rating
    def get_sustainability_rating(self, df, portfolio):
        sustainability_rating = 0
        carbon_score = 0
        for ticker in portfolio:
            sustainability_rating += df[self.df['TICKER'] == ticker]['Sustainability_Rating'].iloc[0]
            carbon_score += df[self.df['TICKER'] == ticker]['Carbon_Footprint'].iloc[0]
        sustainability_rating = round(sustainability_rating / len(portfolio), 2)
        carbon_score = round(carbon_score / len(portfolio), 2)
        return sustainability_rating, carbon_score

    # Recommend Tickers based on the percent of change
    def recommend_tickers(self):
        self.current_sustainability_rating, self.current_carbon_footprint = client.get_sustainability_rating(self.df,
                                                                                                         self.portfolio_user_1)
        self.current_normalized_score = self.normalize_carbon_score(self.current_carbon_footprint)
        number_of_tickers_to_recommend = round((self.percent_of_change / 100) * len(self.portfolio_user_1))
        print("The number of tickers that the user wants to change in the portfolio: ", number_of_tickers_to_recommend)
        df_without_portfolio_tickers = self.filter_rows_by_values(self.df, "TICKER", self.portfolio_user_1)
        self.potential_df = df_without_portfolio_tickers.nsmallest(number_of_tickers_to_recommend,
                                                                     ['Carbon_Footprint'])

    def splitDict(self, d, size):
        n = size
        i = iter(d.items())
        d1 = dict(itertools.islice(i, n))
        d2 = dict(i)
        return d1, d2

    # Create a bar graph showing the differences
    def bar_graph_recommendations(self, original_portfolio, potential_portfolio, number_of_tickers_changing):
        # set width of bar
        barWidth = 0.25

        dictionary_original_portfolios = {}
        dictionary_potential_portfolios = {}

        for i in range(len(original_portfolio) - number_of_tickers_changing, len(original_portfolio)):
            dictionary_original_portfolios[original_portfolio[i][0]] = original_portfolio[i][1]

        for i in range(len(potential_portfolio) - number_of_tickers_changing, len(potential_portfolio)):
            dictionary_potential_portfolios[potential_portfolio[i][0]] = potential_portfolio[i][1]

        original_bars = [[0]]
        potential_bars = [[1.50]]

        # Set position of bar on X axis
        for i in range(0, len(dictionary_original_portfolios)):
            list_orig = [x + barWidth for x in original_bars[i]]
            original_bars.append(list_orig)

        for i in range(0, len(dictionary_original_portfolios)):
            list_recom = [x + barWidth for x in potential_bars[i]]
            potential_bars.append(list_recom)

        # Make the plot
        colors_orig = ['black', 'red', 'magenta', 'blue']
        colors_potential = ['green', 'yellow', 'cyan']

        for index, (key, value) in enumerate(dictionary_original_portfolios.items()):
            plt.bar(original_bars[index], value, color=colors_orig[index], width=barWidth, edgecolor='grey', label=key)

        for index, (key, value) in enumerate(dictionary_potential_portfolios.items()):
            plt.bar(potential_bars[index], value, color=colors_potential[index], width=barWidth, edgecolor='grey',
                    label=key)

        # Adding Xticks
        plt.xlabel('Tickers', fontweight='bold', fontsize=15)
        plt.ylabel('Carbon Footprint (tCO\u2082e/mUSD)', fontweight='bold', fontsize=15)
        plt.xticks([original_bars[1][0], potential_bars[1][0]],
                   ['Original Portfolio', 'potential Portfolio'])
        plt.legend()
        plt.show()

    # Changing the portfolio to potential portfolio
    def change_portfolio(self):
        self.recommend_tickers()
        carbon_footprint = {}
        for ticker in self.portfolio_user_1:
            carbon_footprint[ticker] = self.df.loc[self.df['TICKER'] == ticker]['Carbon_Footprint'].iloc[0]
        sorted_portfolio_user_1 = sorted(carbon_footprint.items(), key=lambda item: item[1])
        removed_portfolio_user_1 = sorted_portfolio_user_1[:len(self.portfolio_user_1) - len(self.potential_df)]
        for index, row in self.potential_df.iterrows():
            removed_portfolio_user_1.append((row['TICKER'], row['Carbon_Footprint']))
        set1 = set(sorted_portfolio_user_1)
        set2 = set(removed_portfolio_user_1)
        diff_tickers_dict = dict(sorted(dict(set1 ^ set2).items(), key=lambda item: item[1]))
        potential_ticker, portfolio_tickers = self.splitDict(diff_tickers_dict, len(self.potential_df))
        print("The tickers in the portfolio changing are: ", ','.join(list(portfolio_tickers.keys())))
        print("The potential tickers are: ", ','.join(list(potential_ticker.keys())))
        self.bar_graph_recommendations(sorted_portfolio_user_1, removed_portfolio_user_1, len(self.potential_df))
        for ticker in removed_portfolio_user_1:
            self.potential_portfolio.append(ticker[0])
        self.expected_sustainability_rating, self.expected_carbon_footprint = self.get_sustainability_rating(self.df,
                                                                                                         self.potential_portfolio)
        self.expected_normalized_score = self.normalize_carbon_score(self.expected_carbon_footprint)
        self.print_portfolio()

    def print_portfolio(self):
        print("##################################################################")
        print("The current portfolio of the user is: ", ",".join(self.portfolio_user_1))
        print("The current sustainability rating is: ", self.current_sustainability_rating)
        print("The current carbon score is: ", self.current_normalized_score)
        print("The average carbon footprint for the portfolio is: ", self.current_carbon_footprint)

        print("##################################################################")
        print("The percentage of change to the portfolio as requested by the user: ", self.percent_of_change, "%")

        print("##################################################################")
        print("The potential portfolio of the user is: ", ",".join(self.potential_portfolio))
        print("The potential sustainability rating is: ", self.expected_sustainability_rating)
        print("The potential carbon score is: ", self.expected_normalized_score)
        print("The average carbon footprint for the potential portfolio is: ", self.expected_carbon_footprint)

        print("##################################################################")
        print("******************************************************************")
        print("The sustainability rating has increased by ",
              "{:.2f}".format(((
              self.expected_sustainability_rating - self.current_sustainability_rating) / self.current_sustainability_rating) * 100),
              "%")
        print("The carbon footprint score has increased by ",
              "{:.2f}".format(
                  ((self.expected_normalized_score - self.current_normalized_score) / self.current_normalized_score) * 100), "%")
        print("The potential portfolio has reduced ~",
              math.ceil(self.current_carbon_footprint - self.expected_carbon_footprint),
              "tonnes of carbon dioxide per million USD")
        print("******************************************************************")

        print("##################################################################")


# Working as a user
client = Recommend_Carbon_Portfolio()

# Increase in the sustainability rating with the added change in portfolio
client.change_portfolio()

# Graph with two lines


# Tangible impact based on city sqft and WACI
