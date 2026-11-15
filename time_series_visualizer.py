import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import calendar
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value'] <= df['value'].quantile(0.975)) & (df['value'] >= df['value'].quantile(0.025))]

def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))

    plot = sns.lineplot(
        data=df,
        x='date',
        y='value',
        ax=ax,
    )

    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby(
    [df.index.year, df.index.month]
        )['value'].mean().unstack()

    # Draw bar plot
    df_bar.columns = [calendar.month_name[m] for m in df_bar.columns]
    
    fig, ax = plt.subplots(figsize=(12, 6))

    df_bar.plot(kind='bar', ax=ax)

    ax.set(xlabel='Years', ylabel='Average Page Views')
    ax.legend(title='Months')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15,6))

    sns.boxplot(
        data=df_box,
        x='year',
        y='value',
        ax=ax[0],
        palette='deep',
        legend=False,
        hue='year'
    )

    sns.boxplot(
        data=df_box,
        x='month',
        y='value',
        ax=ax[1],
        order=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
       'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
       palette='pastel',
       legend=False,
       hue='month'
    )
    
    ax[0].set(xlabel='Year', ylabel='Page Views', title='Year-wise Box Plot (Trend)')
    ax[1].set(xlabel='Month', ylabel='Page Views', title='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

