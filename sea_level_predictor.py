import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Create first line of best fit
    y = range(2014, 2051)
    x = {'Year': list(y)}
    new_year = pd.DataFrame(x)
    df_new = df.append(new_year, ignore_index = True)
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_pred = intercept + slope * df_new['Year']
    plt.plot(df_new['Year'],y_pred, color="red")
    
    # Create second line of best fit
    i = df_new[(df_new['Year'] < 2000)].index
    df_new.drop(i, inplace=True)
    plt.scatter(df_new['Year'], df_new['CSIRO Adjusted Sea Level'])
    slope, intercept, r, p, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    y_pred = intercept + slope * df_new['Year']
    plt.plot(df_new['Year'],y_pred, color="red")

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()