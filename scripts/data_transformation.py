import pandas as pd

def txt_to_csv(txt_file, csv_file, delimiter='\t', header=True):
    """
    Convert a TXT file to a CSV file.

    Parameters:
    - txt_file: str, path to the input TXT file.
    - csv_file: str, path to the output CSV file.
    - delimiter: str, the delimiter used in the TXT file (default is tab).
    - header: bool, whether the first row of the TXT file is a header (default is True).
    """
    try:
        # Read the TXT file
        if header:
            df = pd.read_csv(txt_file, delimiter=delimiter)
        else:
            df = pd.read_csv(txt_file, delimiter=delimiter, header=None)
        
        # Save the DataFrame as a CSV file
        df.to_csv(csv_file, index=False)
        print(f"Successfully converted '{txt_file}' to '{csv_file}'")
    
    except Exception as e:
        print(f"Error occurred: {e}")


