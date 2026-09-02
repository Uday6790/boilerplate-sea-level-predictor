import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Create years from first year through 2050
    years = pd.Series(range(df["Year"].min(), 2051))

    # Calculate predicted sea levels
    predicted_sea_level = slope * years + intercept

    # Plot first line of best fit
    plt.plot(years, predicted_sea_level)

    # Use data from year 2000 onward
    df_recent = df[df["Year"] >= 2000]

    # Line of best fit for data from 2000 onward
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    # Create years from 2000 through 2050
    years_recent = pd.Series(range(2000, 2051))

    # Calculate predicted sea levels
    predicted_recent = slope_recent * years_recent + intercept_recent

    # Plot second line of best fit
    plt.plot(years_recent, predicted_recent)

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save and return the plot
    plt.savefig("sea_level_plot.png")
    return plt.gca()