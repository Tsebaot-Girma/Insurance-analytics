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