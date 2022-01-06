import pandas as pd
import itertools
import matplotlib.pyplot as plt

df = pd.read_csv("Data_populated.csv", index_col=False)

portfolio_user_1 = ["AZ", "BL", "AP", "G", "H"]  # Portfolio Tickers


# Subset of df
def filter_rows_by_values(df, col, values):
    return df[~df[col].isin(values)]


# Normalize Carbon Score
def normalize_carbon_score(score, df, length_portfolio):
    max_value = df['Carbon_Footprint'].max() / length_portfolio
    min_value = df['Carbon_Footprint'].min() / length_portfolio
    normalized_score = (score - min_value) / (max_value - min_value)
    return round(10 - normalized_score, 2)


# Current Sustainability Rating
def get_sustainability_rating(df, portfolio_user_1):
    sustainability_rating = 0
    carbon_score = 0
    for ticker in portfolio_user_1:
        sustainability_rating += df.loc[df['TICKER'] == ticker]['Sustainability_Rating'].iloc[0]
        carbon_score += df.loc[df['TICKER'] == ticker]['Carbon_Footprint'].iloc[0]
    current_sustainability_rating = sustainability_rating / len(portfolio_user_1)
    current_carbon_score = carbon_score / len(portfolio_user_1)
    return round(current_sustainability_rating, 2), round(current_carbon_score, 2)


# Recommend Tickers based on the percent of change
def recommend_tickers(percent_of_change, portfolio_user_1, df):
    number_of_tickers_to_recommend = round((percent_of_change / 100) * len(portfolio_user_1))
    print("The number of tickers that the user wants in the portfolio to be changed: ", number_of_tickers_to_recommend)
    df_without_portfolio_tickers = filter_rows_by_values(df, "TICKER", portfolio_user_1)
    recommended_df = df_without_portfolio_tickers.nsmallest(number_of_tickers_to_recommend, ['Carbon_Footprint'])
    print("The recommended tickers to change in the portfolio are:",
          recommended_df['TICKER'].to_string(index=False).replace("\n", ","))
    return recommended_df


def splitDict(d, size):
    n = size
    i = iter(d.items())
    d1 = dict(itertools.islice(i, n))
    d2 = dict(i)
    return d1, d2


# Create a bar graph showing the differences
def bar_graph_recommendations(original_portfolio, recommended_portfolio, number_of_tickers_changing):
    # set width of bar
    barWidth = 0.25

    dictionary_original_portfolios = {}
    dictionary_recommended_portfolios = {}

    for i in range(len(original_portfolio) - number_of_tickers_changing, len(original_portfolio)):
        dictionary_original_portfolios[original_portfolio[i][0]] = original_portfolio[i][1]

    for i in range(len(recommended_portfolio) - number_of_tickers_changing, len(recommended_portfolio)):
        dictionary_recommended_portfolios[recommended_portfolio[i][0]] = recommended_portfolio[i][1]

    original_bars = [[0]]
    recommended_bars = [[1.50]]

    # Set position of bar on X axis
    for i in range(0, len(dictionary_original_portfolios)):
        list_orig = [x + barWidth for x in original_bars[i]]
        original_bars.append(list_orig)

    for i in range(0, len(dictionary_original_portfolios)):
        list_recom = [x + barWidth for x in recommended_bars[i]]
        recommended_bars.append(list_recom)

    # Make the plot
    colors_orig = ['black', 'red', 'magenta', 'blue']
    colors_recommended = ['green', 'yellow', 'cyan']

    for index, (key, value) in enumerate(dictionary_original_portfolios.items()):
        plt.bar(original_bars[index], value, color=colors_orig[index], width=barWidth, edgecolor='grey', label=key)

    for index, (key, value) in enumerate(dictionary_recommended_portfolios.items()):
        plt.bar(recommended_bars[index], value, color=colors_recommended[index], width=barWidth, edgecolor='grey',
                label=key)

    # Adding Xticks
    plt.xlabel('Tickers', fontweight='bold', fontsize=15)
    plt.ylabel('Carbon Footprint', fontweight='bold', fontsize=15)
    plt.xticks([original_bars[1][0], recommended_bars[1][0]],
               ['Original Portfolio', 'Recommended Portfolio'])
    plt.legend()
    plt.show()


# Changing the portfolio to recommended portfolio
def change_portfolio(recommended_df, df, portfolio_user_1):
    carbon_footprint = {}
    for ticker in portfolio_user_1:
        carbon_footprint[ticker] = df.loc[df['TICKER'] == ticker]['Carbon_Footprint'].iloc[0]
    sorted_portfolio_user_1 = sorted(carbon_footprint.items(), key=lambda item: item[1])
    removed_portfolio_user_1 = sorted_portfolio_user_1[:len(portfolio_user_1) - len(recommended_df)]
    for index, row in recommended_df.iterrows():
        removed_portfolio_user_1.append((row['TICKER'], row['Carbon_Footprint']))
    set1 = set(sorted_portfolio_user_1)
    set2 = set(removed_portfolio_user_1)
    diff_tickers_dict = dict(sorted(dict(set1 ^ set2).items(), key=lambda item: item[1]))
    recommended_ticker, portfolio_tickers = splitDict(diff_tickers_dict, len(recommended_df))
    print("The portfolio tickers recommended to be replaced are: ", ','.join(list(portfolio_tickers.keys())))
    bar_graph_recommendations(sorted_portfolio_user_1, removed_portfolio_user_1, len(recommended_df))
    changed_portfolio_user_1 = []
    for ticker in removed_portfolio_user_1:
        changed_portfolio_user_1.append(ticker[0])
    expected_sustainability_rating, expected_carbon_score = get_sustainability_rating(df, changed_portfolio_user_1)
    print("The increased sustainability rating will be: ", expected_sustainability_rating)
    print("The increased carbon score is: ",
          normalize_carbon_score(expected_carbon_score, df, len(changed_portfolio_user_1)))
    print("The decreased average carbon footprint for the recommended portfolio is: ", expected_carbon_score)


# Working as a user
current_sustainability_rating, current_carbon_score = get_sustainability_rating(df, portfolio_user_1)
print("The current sustainability rating is: ", current_sustainability_rating)
print("The current carbon score is: ", normalize_carbon_score(current_carbon_score, df, len(portfolio_user_1)))
print("The average carbon footprint for the portfolio is: ", current_carbon_score)

# Better Combination of Tickers for higher Sustainability Rating based on % of change
percent_of_change = int(input("Enter the percentage of change to the portfolio: "))
print("The percentage of change to the portfolio as requested by the user: ", percent_of_change, "%")
recommended_df = recommend_tickers(percent_of_change, portfolio_user_1, df)

# Increase in the sustainability rating with the added change in portfolio
change_portfolio(recommended_df, df, portfolio_user_1)

# Graph with two lines


# Tangible impact based on city sqft and WACI
