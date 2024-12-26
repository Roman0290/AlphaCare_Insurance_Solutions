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
