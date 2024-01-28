import pandas as pd
import sys
import json

def create_dataframes(form_data):
    # Parse the JSON-formatted form data
    try:
        form_data_dict = json.loads(form_data)
    except json.JSONDecodeError as e:
        print("Error decoding JSON:", e)
        return
    
    # Define column names for each DataFrame
    adhd_columns = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18']
    anxiety_columns = ['Q24', 'Q25', 'Q26']
    mania_columns = ['Q22', 'Q23']
    anger_columns = ['Q21']
    psychosis_columns = ['Q30', 'Q31']
    somatic_columns = ['Q27', 'Q28']
    substance_use_columns = ['Q33', 'Q34', 'Q35']
    suicidal_columns = ['Q29']
    did_columns = ['Q32']
    depression_columns = ['Q19', 'Q20']
    dep_qids_columns = ['QSR1', 'QSR2', 'QSR3', 'QSR4', 'QSR5', 'QSR6', 'QSR7', 'QSR8', 'QSR9', 'QSR10', 'QSR11', 'QSR12', 'QSR13', 'QSR15', 'QSR16']
    
    # Create dictionaries to hold the responses for each question
    adhd_responses = {}
    anxiety_responses = {}
    mania_responses = {}
    anger_responses = {}
    psychosis_responses = {}
    somatic_responses = {}
    substance_use_responses = {}
    suicidal_responses = {}
    did_responses = {}
    depression_responses = {}
    dep_qids_responses = {}

    # Iterate over form data responses
    for question_id, selected_option in form_data_dict.items():
        # Check the question ID and add the selected option to the appropriate dictionary
        if question_id in adhd_columns:
            adhd_responses[question_id] = selected_option
        elif question_id in anxiety_columns:
            anxiety_responses[question_id] = selected_option
        elif question_id in mania_columns:
            mania_responses[question_id] = selected_option
        elif question_id in anger_columns:
            anger_responses[question_id] = selected_option
        elif question_id in psychosis_columns:
            psychosis_responses[question_id] = selected_option
        elif question_id in somatic_columns:
            somatic_responses[question_id] = selected_option
        elif question_id in substance_use_columns:
            substance_use_responses[question_id] = selected_option
        elif question_id in suicidal_columns:
            suicidal_responses[question_id] = selected_option
        elif question_id in did_columns:
            did_responses[question_id] = selected_option
        elif question_id in depression_columns:
            depression_responses[question_id] = selected_option
        elif question_id in dep_qids_columns:
            dep_qids_responses[question_id] = selected_option
    
    # Create DataFrames from the dictionaries
    input_variables_ADHD = pd.DataFrame(adhd_responses, index=[0])
    input_variables_Anxiety = pd.DataFrame(anxiety_responses, index=[0])
    input_variables_MANIA = pd.DataFrame(mania_responses, index=[0])
    input_variables_ANGER = pd.DataFrame(anger_responses, index=[0])
    input_variables_PSYCHOSIS = pd.DataFrame(psychosis_responses, index=[0])
    input_variables_SOMATIC = pd.DataFrame(somatic_responses, index=[0])
    input_variables_SUBSTANCE_USE = pd.DataFrame(substance_use_responses, index=[0])
    input_variables_SUICIDAL = pd.DataFrame(suicidal_responses, index=[0])
    input_variables_DID = pd.DataFrame(did_responses, index=[0])
    input_variables_Depression = pd.DataFrame(depression_responses, index=[0])
    input_variables_DEP_QIDS = pd.DataFrame(dep_qids_responses, index=[0])

    # Write DataFrames to CSV files
    input_variables_ADHD.to_csv('../pythonApi/inputFiles/input_variables_ADHD.csv', index=False)
    input_variables_Anxiety.to_csv('../pythonApi/inputFiles/input_variables_Anxiety.csv', index=False)
    input_variables_MANIA.to_csv('../pythonApi/inputFiles/input_variables_MANIA.csv', index=False)
    input_variables_ANGER.to_csv('../pythonApi/inputFiles/input_variables_ANGER.csv', index=False)
    input_variables_PSYCHOSIS.to_csv('../pythonApi/inputFiles/input_variables_PSYCHOSIS.csv', index=False)
    input_variables_SOMATIC.to_csv('../pythonApi/inputFiles/input_variables_SOMATIC.csv', index=False)
    input_variables_SUBSTANCE_USE.to_csv('../pythonApi/inputFiles/input_variables_SUBSTANCE_USE.csv', index=False)
    input_variables_SUICIDAL.to_csv('../pythonApi/inputFiles/input_variables_SUICIDAL.csv', index=False)
    input_variables_DID.to_csv('../pythonApi/inputFiles/input_variables_DID.csv', index=False)
    input_variables_Depression.to_csv('../pythonApi/inputFiles/input_variables_Depression.csv', index=False)
    input_variables_DEP_QIDS.to_csv('../pythonApi/inputFiles/input_variables_DEP_QIDS.csv', index=False)
    

if __name__ == "__main__":
    # Read form data from standard input
    form_data = sys.stdin.read()
    
    # Debugging: Print form data to inspect its contents
    print("Form Data:", form_data)

    # Create DataFrames and write to CSV files
    create_dataframes(form_data)
