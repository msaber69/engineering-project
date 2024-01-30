import pandas as pd
import sys
import json
import os

def create_dataframes(form_data):
    # Parse the JSON-formatted form data
    try:
        form_data_dict = json.loads(form_data)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return
    
    # Define column names for each DataFrame
    columns_mapping = {
        'ADHD': ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18'],
        'Anxiety': ['Q24', 'Q25', 'Q26'],
        'Mania': ['Q22', 'Q23'],
        'Anger': ['Q21'],
        'Psychosis': ['Q30', 'Q31'],
        'Somatic': ['Q27', 'Q28'],
        'Substance_Use': ['Q33', 'Q34', 'Q35'],
        'Suicidal': ['Q29'],
        'DID': ['Q32'],
        'Depression': ['Q19', 'Q20'],
        'Dep_QIDS': ['QSR1', 'QSR2', 'QSR3', 'QSR4', 'QSR5', 'QSR6', 'QSR7', 'QSR8', 'QSR9', 'QSR10', 'QSR11', 'QSR12', 'QSR13', 'QSR15', 'QSR16']
    }

    # Path to the directory containing CSV files
    csv_directory = '../pythonApi/inputFiles/'

    # Iterate over each type of data and its columns
    for data_type, columns in columns_mapping.items():
        # Construct the CSV file path
        csv_file = os.path.join(csv_directory, f'input_variables_{data_type}.csv')

        # Check if there are any responses for the current dataframe
        if any(form_data_dict.get(col) for col in columns):
            # Append new row with form data
            new_data = pd.DataFrame([form_data_dict], columns=columns)
            
            # Check if the CSV file exists and contains data
            if os.path.isfile(csv_file) and os.path.getsize(csv_file) > 0:
                # Read existing data from CSV file
                try:
                    existing_data = pd.read_csv(csv_file)
                    # Append new row with form data
                    existing_data = pd.concat([existing_data, new_data], ignore_index=True)
                    existing_data.to_csv(csv_file, index=False)
                except pd.errors.EmptyDataError:
                    print(f"Warning: Empty or invalid CSV file found for {data_type}")
                    # Initialize existing_data as an empty DataFrame
                    existing_data = pd.DataFrame(columns=columns)
                    # Append new row with form data
                    existing_data = pd.concat([existing_data, new_data], ignore_index=True)
                    existing_data.to_csv(csv_file, index=False)
            else:
                # If CSV file doesn't exist or is empty, create new file and write new data
                new_data.to_csv(csv_file, index=False)

if __name__ == "__main__":
    # Read form data from standard input
    form_data = sys.stdin.read()
    
    # Debugging: Print form data to inspect its contents
    print("Form Data:", form_data)

    # Create DataFrames and append to CSV files
    create_dataframes(form_data)
