import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load data from a .txt file and convert it to a .csv file."""
    output_file = file_path.replace('.txt', '.csv')
    
    try:
        # Read the .txt file using '|' as the delimiter
        data = pd.read_csv(file_path, delimiter='|')
        
        # Save the DataFrame to a .csv file
        data.to_csv(output_file, index=False)
        
        print(f"File successfully converted and saved as {output_file}")
        return data
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: No data found in the file.")
    except pd.errors.ParserError:
        print("Error: There was a problem parsing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def descriptive_stats(df):
    """Return descriptive statistics of the DataFrame."""
    return df.describe()

def check_missing_values(df):
    """Check for missing values in the DataFrame."""
    return df.isnull().sum()

def plot_histograms(df):
    """Plot histograms for numerical columns."""
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[numerical_cols].hist(bins=15, figsize=(15, 10))
    plt.show()

def plot_boxplots(df):
    """Plot boxplots for numerical columns to detect outliers."""
    numerical_cols = df.select_dtypes(include=['float64', 'int64']).columns
    for col in numerical_cols:
        plt.figure(figsize=(10, 5))
        sns.boxplot(y=df[col])
        plt.title(f'Box plot of {col}')
        plt.show()

def plot_scatter(df, x, y):
    """Plot a scatter plot between two variables."""
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=x, y=y)
    plt.title(f'Scatter plot between {x} and {y}')
    plt.show()