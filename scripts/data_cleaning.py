import pandas as pd

def clean_csv(file_path, output_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Inspect the data
    print("Initial DataFrame:")
    print(df.head())  # Changed to call head() method

    # Print the actual column names
    print("Columns in DataFrame:")
    print(df.columns)

    # Trim whitespaces from column names
    df.columns = df.columns.str.strip()

    # Handle missing values
    missing_before = df.isnull().sum().sum()  # Count total missing values before cleaning
    df.dropna(inplace=True)
    missing_after = df.isnull().sum().sum()   # Count total missing values after cleaning

    # Remove duplicates
    duplicates_before = df.duplicated().sum()  # Count duplicates before removing
    df.drop_duplicates(inplace=True)
    duplicates_after = df.duplicated().sum()   # Count duplicates after removing

    # Print summary of cleaning operations
    print(f"Total missing values before cleaning: {missing_before}")
    print(f"Total missing values after cleaning: {missing_after}")
    print(f"Total duplicates before cleaning: {duplicates_before}")
    print(f"Total duplicates after cleaning: {duplicates_after}")

    # Save the cleaned DataFrame to a new CSV file
    df.to_csv(output_path, index=False)
    print(f"Cleaned data saved to '{output_path}'")

def check_missing_values(file_path):
    # Load the data
    df = pd.read_csv(file_path)

    # Check for missing values in each column
    missing_values = df.isnull().sum()

    # Filter to show only columns with missing values
    missing_values = missing_values[missing_values > 0]

    # Display the results
    if not missing_values.empty:
        print("Columns with missing values:")
        print(missing_values)
    else:
        print("No missing values in any column.")

# Example usage
# if __name__ == "__main__":
#     input_file = 'your_data.csv'  
#     output_file = 'cleaned_data.csv'  
#     check_missing_values(input_file)  
#     clean_csv(input_file, output_file)  
import matplotlib.pyplot as plt
import seaborn as sns

import missingno as msno


def missingno(data):
    msno.matrix(data, figsize=(10, 6), color=(0.25, 0.5, 0.9))  # Adjust size and color
    plt.title("Missing Data Visualization", fontsize=16)

    plt.xticks(
        range(data.shape[1]),          
        data.columns,                  
        rotation=90, fontsize=10        
    )
    plt.show()


def missing_percentage_all(data):
    missing_percentage = (data.isnull().sum() / len(data)) * 100
   
    return missing_percentage


def missing_percentage(data, thresholds):
    missing_percentage = (data.isnull().sum() / len(data)) * 100
    missing_columns_percentage = missing_percentage[missing_percentage > thresholds]
    return missing_columns_percentage

def remove_missing_row(data, thresholds):
    missing_percentage = (data.isnull().sum()/ len(data)*100)
    missing_columns_percentage = missing_percentage[missing_percentage < thresholds].index
    
    data = data.dropna(subset=missing_columns_percentage)
    
    return data
    
def fill_missing_values(data):
    data['Bank'] = data['Bank'].fillna(data['Bank'].mode()[0])
    data['NewVehicle'] = data['NewVehicle'].fillna(data['Bank'].mode()[0])
    data['AccountType'] = data['AccountType'].fillna(data['Bank'].mode()[0])
    data['MaritalStatus'] = data['MaritalStatus'].fillna(data['MaritalStatus'].mode()[0])
    data['Gender'] = data['Gender'].fillna(data['Gender'].mode()[0])
    return data

def drop_column(data, column_to_drop):
    data = data.drop(columns=column_to_drop,inplace=True)
    return data


def identify_outliers(data, columns):
    outliers = {}

    for column in columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identify outliers
        outliers[column] = data[(data[column] < lower_bound) | (data[column] > upper_bound)]


    return outliers

# Cap and floor outliers for all numeric columns
def cap_outliers(data, columns):
    for column in columns:
        Q1 = data[column].quantile(0.25)
        Q3 = data[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        data[column] = data[column].clip(lower=lower_bound, upper=upper_bound)
    return data