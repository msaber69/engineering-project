import pandas as pd
import sys
import os

# Define function to fill input files from test responses
def fill_input_files():
    # Path to the directory containing CSV files
    csv_directory = '../server/'

    # Read test1 responses
    test1_file = os.path.join(csv_directory, 'test1_responses.csv')
    test1_responses = pd.read_csv(test1_file, header=None)
    test1_responses = test1_responses.iloc[0]

    # Read test2 responses
    test2_file = os.path.join(csv_directory, 'test2_responses.csv')
    test2_responses = pd.read_csv(test2_file, header=None)
    test2_responses = test2_responses.iloc[0]

    # Read test3 responses
    test3_file = os.path.join(csv_directory, 'test3_responses.csv')
    test3_responses = pd.read_csv(test3_file, header=None)
    test3_responses = test3_responses.iloc[0]

    # Extract responses for each input variable and create DataFrames
    input_variables_ADHD = pd.DataFrame([test1_responses.iloc[:18]], columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18'])
    input_variables_Anxiety = pd.DataFrame([test1_responses.iloc[23:26]], columns=['Q24', 'Q25', 'Q26'])
    input_variables_MANIA = pd.DataFrame([test1_responses.iloc[21:23]], columns=['Q22', 'Q23'])
    input_variables_ANGER = pd.DataFrame([test1_responses.iloc[20]], columns=['Q21'])
    input_variables_PSYCHOSIS = pd.DataFrame([test1_responses.iloc[28:30]], columns=['Q30', 'Q31'])
    input_variables_SOMATIC = pd.DataFrame([test1_responses.iloc[26:28]], columns=['Q27', 'Q28'])
    input_variables_SUBSTANCE_USE = pd.DataFrame([test1_responses.iloc[30:33]], columns=['Q33', 'Q34', 'Q35'])
    input_variables_SUICIDAL = pd.DataFrame([test1_responses.iloc[29]], columns=['Q29'])
    input_variables_DID = pd.DataFrame([test1_responses.iloc[31]], columns=['Q32'])
    input_variables_Depression = pd.DataFrame([test1_responses.iloc[18:20]], columns=['Q19', 'Q20'])
    input_variables_DEP_QIDS = pd.DataFrame([test3_responses], columns=['QSR1', 'QSR2', 'QSR3', 'QSR4', 'QSR5', 'QSR6', 'QSR7', 'QSR8', 'QSR9', 'QSR10', 'QSR11', 'QSR12', 'QSR13', 'QSR14', 'QSR15', 'QSR16'])
    
    # Write DataFrames to input files
    input_variables_ADHD.to_csv(os.path.join(csv_directory, 'input_variables_ADHD.csv'), index=False)
    input_variables_Anxiety.to_csv(os.path.join(csv_directory, 'input_variables_Anxiety.csv'), index=False)
    input_variables_MANIA.to_csv(os.path.join(csv_directory, 'input_variables_MANIA.csv'), index=False)
    input_variables_ANGER.to_csv(os.path.join(csv_directory, 'input_variables_ANGER.csv'), index=False)
    input_variables_PSYCHOSIS.to_csv(os.path.join(csv_directory, 'input_variables_PSYCHOSIS.csv'), index=False)
    input_variables_SOMATIC.to_csv(os.path.join(csv_directory, 'input_variables_SOMATIC.csv'), index=False)
    input_variables_SUBSTANCE_USE.to_csv(os.path.join(csv_directory, 'input_variables_SUBSTANCE_USE.csv'), index=False)
    input_variables_SUICIDAL.to_csv(os.path.join(csv_directory, 'input_variables_SUICIDAL.csv'), index=False)
    input_variables_DID.to_csv(os.path.join(csv_directory, 'input_variables_DID.csv'), index=False)
    input_variables_Depression.to_csv(os.path.join(csv_directory, 'input_variables_Depression.csv'), index=False)
    input_variables_DEP_QIDS.to_csv(os.path.join(csv_directory, 'input_variables_DEP_QIDS.csv'), index=False)

# Execute function to fill input files
fill_input_files()
