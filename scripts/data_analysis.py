import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math

def descriptive_stats(df):
    """Return descriptive statistics of the DataFrame."""
    return df.describe()

def check_missing_values(df):
    """Check for missing values in the DataFrame."""
    return df.isnull().sum()

def plot_histograms(df):
    """Plot histograms for numerical columns."""
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols].hist(bins=15, figsize=(20, 15))
    plt.show()



def plot_bar_charts(df):
    """
    Plot bar charts for categorical columns with fewer than 10 unique categories to understand distributions.
    """
    # Identify categorical columns with fewer than 10 unique categories
    categorical_cols = [
        col for col in df.select_dtypes(include=['object', 'category']).columns
        if df[col].nunique() < 10
    ]

    # Calculate the number of rows and columns for subplots
    num_cols = 3  # Set the number of columns per row
    num_rows = math.ceil(len(categorical_cols) / num_cols)

    # Set up the matplotlib figure with dynamic size
    plt.figure(figsize=(num_cols * 5, num_rows * 4))

    # Create bar plots for each categorical column
    for i, col in enumerate(categorical_cols, 1):
        plt.subplot(num_rows, num_cols, i)  # Arrange subplots in a grid
        value_counts = df[col].value_counts()  # Count the frequency of each category
        sns.barplot(x=value_counts.index, y=value_counts.values)  # Bar chart for each column
        plt.title(f'Bar Chart for {col}')
        plt.xlabel('Categories')
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability

    plt.tight_layout()  # Adjust layout for better readability
    plt.show()


def plot_boxplots(df):
    """Plot boxplots for numerical columns to detect outliers."""
    # Identify numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Set up the matplotlib figure
    plt.figure(figsize=(15, 30))

    # Create box plots for each numerical column
    for i, col in enumerate(numerical_cols, 1):
        plt.subplot(len(numerical_cols), 1, i)  # Create subplots
        sns.boxplot(data=df, y=col)  # Box plot for each numerical column
        plt.title(f'Box Plot for {col}')

    plt.tight_layout()  # Adjust layout for better readability
    plt.show()

def plot_distribution(df):
    """Plot distribution for numerical columns to detect outliers."""

   

    # Set the style of the visualization
    sns.set(style='whitegrid')
    # Identify numerical columns
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns

    # Set up the matplotlib figure
    plt.figure(figsize=(10, 5 * len(numerical_cols)))

    # Create distribution plots for each numerical column
    for i, col in enumerate(numerical_cols, 1):
        plt.subplot(len(numerical_cols), 1, i)  # Create subplots
        sns.histplot(df[col], bins=30, kde=True, color='skyblue')
        plt.title(f"Distribution of {col}", fontsize=16)
        plt.xlabel(col, fontsize=14)
        plt.ylabel('Density', fontsize=14)
        plt.axvline(df[col].mean(), color='red', linestyle='--', label='Mean')
        plt.axvline(df[col].median(), color='green', linestyle='--', label='Median')
        plt.legend(loc='upper right')

    plt.tight_layout()  # Adjust layout for better readability
    plt.show()
def plot_Premium_vs_claims(df):
    #Scatter Plot of TotalPremium vs. TotalClaims
    plt.figure(figsize=(12, 6))
    sns.scatterplot(data=df, x='TotalPremium', y='TotalClaims', hue='PostalCode', palette='viridis', alpha=0.7)
    plt.title('Scatter Plot of TotalPremium vs. TotalClaims by PostalCode')
    plt.xlabel('TotalPremium')
    plt.ylabel('TotalClaims')
    plt.legend(title='PostalCode', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.show()

def Correlation_of_premium_claims(df): 
        correlation_matrix = df[['TotalPremium', 'TotalClaims']].corr()
        print("\nCorrelation Matrix:")
        print(correlation_matrix)

        # Plotting the correlation matrix
        plt.figure(figsize=(6, 4))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
        plt.title('Correlation Matrix of TotalPremium and TotalClaims')
        plt.show()
def postal_code_analysis(df):  
        #Grouping by PostalCode and calculating average TotalPremium and TotalClaims
        postal_code_analysis = df.groupby('PostalCode')[['TotalPremium', 'TotalClaims']].mean().reset_index()
        print("\nAverage TotalPremium and TotalClaims by PostalCode:")
        print(postal_code_analysis)


def cover_type_analysis(df):
    """
    Analyze and visualize the average TotalPremium and TotalClaims by Province and Cover Type.
    """
    # Grouping by Province and Cover Type
    cover_type_analysis = df.groupby(['Province', 'CoverType'], observed=True)[['TotalPremium', 'TotalClaims']].mean().reset_index()

    # Print the description of the analysis
    print("Average TotalPremium and TotalClaims by Province and Cover Type:")
    print(cover_type_analysis)

    # Plotting Cover Type Analysis
    plt.figure(figsize=(24, 10))  # Increased figure size
    sns.barplot(data=cover_type_analysis, x='Province', y='TotalPremium', hue='CoverType', errorbar=None)
    plt.title('Average Total Premium by Province and Cover Type', fontsize=20)  # Larger title font size
    plt.xlabel('Province', fontsize=20)  # Larger x-axis label font size
    plt.ylabel('Average Total Premium', fontsize=20)  # Larger y-axis label font size
    plt.legend(title='Cover Type', bbox_to_anchor=(1.05, 1), loc='upper left')  # Legend outside the plot
    plt.xticks(rotation=45, fontsize=15)  # Larger x-axis tick labels
    plt.tight_layout()  # Adjust layout for better readability
    plt.show()


def auto_make_analysis(df):
    #Grouping by Auto Make
    auto_make_analysis = df.groupby(['make'], observed=True)[['TotalPremium', 'TotalClaims']].mean().reset_index()
    print("\nAverage TotalPremium and TotalClaims by Auto Make:")
    print(auto_make_analysis)
    # Plotting Auto Make Analysis
    plt.figure(figsize=(25, 10))
    sns.barplot(data=auto_make_analysis, x='make', y='TotalPremium', errorbar=None)
    plt.title('Average Total Premium by Auto Make', fontsize=20)
    plt.xlabel('Auto Make', fontsize=20)
    plt.ylabel('Average Total Premium', fontsize=20)
    plt.xticks(rotation=45, fontsize=15)
    plt.tight_layout()
    plt.show()

def time_trend_analysis(df):

    # Group by YearMonth
    df['YearMonth'] = df['TransactionMonth'].dt.to_period('M')
    time_trend_analysis = df.groupby(['YearMonth'], observed=True)[['TotalPremium', 'TotalClaims']].mean().reset_index()

    # Convert YearMonth to datetime
    time_trend_analysis['YearMonth'] = time_trend_analysis['YearMonth'].dt.to_timestamp()

        # Inspect the result
    print("\nInspecting time_trend_analysis DataFrame:")
    print(time_trend_analysis.dtypes)  # Check data types
    print(time_trend_analysis.head())   # Display the first few rows

        # Plotting Trends Over Time
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=time_trend_analysis, x='YearMonth', y='TotalPremium', label='Average Total Premium', marker='o')
    sns.lineplot(data=time_trend_analysis, x='YearMonth', y='TotalClaims', label='Average Total Claims', marker='o')
    plt.title('Trends of Average Total Premium and Total Claims Over Time')
    plt.xlabel('Time (Year-Month)')
    plt.ylabel('Average Amount')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_scatter(df, x, y):
    """Plot a scatter plot between two variables."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f'Scatter plot between {x} and {y}')
    plt.show()

def correlation(df):
    numeric_df = df.select_dtypes(include=['number'])  # Keep only numeric columns
    # Calculate the correlation matrix
    correlation_matrix = numeric_df.corr()
    # Create a heatmap
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', square=True, cbar_kws={"shrink": .8})
    plt.title('Correlation Heatmap', fontsize=16)
    plt.show()


def Province_analysis(df):
    # Set the style of the visualization
    sns.set(style='whitegrid')
    # Create a box plot to compare TotalPremium by Province
    plt.figure(figsize=(12, 6))
    sns.boxplot(data=df, x='Province', y='TotalPremium', hue='Province', palette='Set2', legend=False)
    plt.title('Box Plot of Total Premium by Province', fontsize=16)
    plt.xlabel('Province', fontsize=14)
    plt.ylabel('Total Premium', fontsize=14)
    plt.xticks(rotation=45)
    plt.show()
