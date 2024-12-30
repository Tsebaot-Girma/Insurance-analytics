import pandas as pd
import numpy as np


def clean_data(df):
    """Clean the dataset by handling duplicates, missing values, and dropping unnecessary columns."""
    # Drop duplicates
    df = df.drop_duplicates()

    df['CapitalOutstanding'] = pd.to_numeric(df['CapitalOutstanding'], errors='coerce')


    # Convert timestamps
    timestamp_columns = ['TransactionMonth', 'VehicleIntroDate']
    for col in timestamp_columns:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')

    
    # Convert to categorical
    categorical_cols = [
        'Province', 'CoverType', 'VehicleType', 'Gender', 
        'MaritalStatus', 'Bank', 'AccountType', 'Title', 'Language', 'CrossBorder'
    ]
    for col in categorical_cols:
         if col in df.columns:
            df[col] = df[col].astype('category')

  
    # Handling missing values for categorical columns
    categorical_cols = ['Bank', 'AccountType', 'MaritalStatus', 'Gender', 'VehicleType', 'make', 'Model', 'Cylinders', 
                        'bodytype']  # Ensure you add categorical columns here
    for col in categorical_cols:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)



    # Handling missing values for numeric columns
    numeric_cols = ['CustomValueEstimate', 'mmcode', 'cubiccapacity', 'kilowatts', 'NumberOfDoors', 'VehicleIntroDate', 'CapitalOutstanding']
    for col in numeric_cols:
        if col in df.columns:  # Ensure the column exists
            if df[col].notna().sum() > 0:  # Check for non-empty columns
                median_value = df[col].median()
            else:
                median_value = 0  # Assign default value for completely empty columns
            df[col] = df[col].fillna(median_value)


    # Handling missing values for date columns
    median_date = df['VehicleIntroDate'].median()
    df['VehicleIntroDate'] = df['VehicleIntroDate'].fillna(median_date)

    # Handling missing values for 'CrossBorder' and related columns
    df['CrossBorder'] = df['CrossBorder'].fillna('No')
    df['NewVehicle'] = df['NewVehicle'].fillna('No')
    df['WrittenOff'] = df['WrittenOff'].fillna('No')
    df['Rebuilt'] = df['Rebuilt'].fillna('No')
    df['Converted'] = df['Converted'].fillna('No')

    # Dropping column with all missing values
    df.drop(columns=['NumberOfVehiclesInFleet'], inplace=True)

    # Create missing value flags for selected columns
    df['Bank_missing'] = df['Bank'].isna().astype(int)
    df['AccountType_missing'] = df['AccountType'].isna().astype(int)

    return df



def handle_outliers(df, columns):
    """Replace outliers with mean values."""
    #Outliers capped using 99th percentile and replaced with mean values              
    for col in columns:
        df[col] = np.where(df[col] > df[col].quantile(0.99), df[col].mean(), df[col])
    return df


