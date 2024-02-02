import pandas as pd
import joblib
import sklearn
import json


# Read test responses from CSV files
test1_responses = pd.read_csv("../server/dataset_server/test1_responses.csv", header=None).iloc[0].tolist()
test2_responses = pd.read_csv("../server/dataset_server/test2_responses.csv", header=None).iloc[0].tolist()
test3_responses = pd.read_csv("../server/dataset_server/test3_responses.csv", header=None).iloc[0].tolist()

# Replace the numbers with the responses from test1, test2, and test3
input_variables_ADHD = pd.DataFrame([test1_responses[:18]], 
                                    columns=['Q1', 'Q2', 'Q3', 'Q4', 'Q5', 'Q6', 'Q7', 'Q8', 'Q9', 'Q10', 'Q11', 'Q12', 'Q13', 'Q14', 'Q15', 'Q16', 'Q17', 'Q18'], 
                                    dtype=float, 
                                    index=['input'])
input_variables_Anxiety = pd.DataFrame([test1_responses[23:26]], 
                                       columns=['Q24', 'Q25', 'Q26'], 
                                       dtype=float, 
                                       index=['input'])
input_variables_MANIA = pd.DataFrame([test1_responses[21:23]], 
                                     columns=['Q22', 'Q23'], 
                                     dtype=float, 
                                     index=['input'])
input_variables_ANGER = pd.DataFrame([test1_responses[20]], 
                                     columns=['Q21'], 
                                     dtype=float, 
                                     index=['input'])
input_variables_PSYCHOSIS = pd.DataFrame([test1_responses[28:30]], 
                                         columns=['Q30', 'Q31'], 
                                         dtype=float, 
                                         index=['input'])
input_variables_SOMATIC = pd.DataFrame([test1_responses[26:28]], 
                                       columns=['Q27', 'Q28'], 
                                       dtype=float, 
                                       index=['input'])
input_variables_SUBSTANCE_USE = pd.DataFrame([test1_responses[30:33]], 
                                             columns=['Q33', 'Q34', 'Q35'], 
                                             dtype=float, index=['input'])
input_variables_SUICIDAL = pd.DataFrame([test1_responses[29]], 
                                        columns=['Q29'], 
                                        dtype=float, 
                                        index=['input'])
input_variables_DID = pd.DataFrame([test1_responses[31]], 
                                   columns=['Q32'], 
                                   dtype=float, 
                                   index=['input'])
input_variables_Depression = pd.DataFrame([test1_responses[18:20]], 
                                          columns=['Q19', 'Q20'], 
                                          dtype=float, index=['input'])
input_variables_DEP_QIDS = pd.DataFrame([test3_responses], 
                                        columns=['QSR1', 'QSR2', 'QSR3', 'QSR4', 'QSR5', 'QSR6', 'QSR7', 'QSR8', 'QSR9', 'QSR10', 'QSR11', 'QSR12', 'QSR13', 'QSR14', 'QSR15', 'QSR16'], 
                                        dtype=float, 
                                        index=['input'])


# Functions
def compute_final_score_ADHD(data):
    # Initialize empty lists to store scores for each row
    Final_ADHD_scores = []
    Inattention_scores = []
    Hyperactivity_scores = []
    Final_ADHD_percentages = []
    Inattention_percentages = []
    Hyperactivity_percentages = []
    
    for idx, row in data.iterrows():
        ## Scoring all the 18 questions:
        # Conditions for Q1, Q2, Q3, Q9, Q12, Q16, and Q18
        condition_1 = int(row['Q1'] > 2) + int(row['Q2'] > 2) + int(row['Q3'] > 2) + int(row['Q9'] > 2) + int(row['Q12'] > 2) + int(row['Q16'] > 2) + int(row['Q18'] > 2)

        # Conditions for Q4, Q5, Q6, Q7, Q8, Q10, Q11, Q13, Q14, Q15, Q17
        condition_2 = int(row['Q4'] > 3) + int(row['Q5'] > 3) + int(row['Q6'] > 3) + int(row['Q7'] > 3) + int(row['Q8'] > 3) + int(row['Q10'] > 3) + int(row['Q11'] > 3) + int(row['Q13'] > 3) + int(row['Q14'] > 3) + int(row['Q15'] > 3) + int(row['Q17'] > 3)

        ## Differentiate between ADD (Inattention) and ADHD (Inattention+hyper):
        # 1. Inattention

        # Conditions for Q1,Q2,Q3,Q9
        condition_3 = int(row['Q1'] > 2) + int(row['Q2'] > 2) + int(row['Q3'] > 2) + int(row['Q9'] > 2)

        # Conditions for Q4,Q7,Q8,Q10,Q11
        condition_4 = int(row['Q4'] > 3) + int(row['Q7'] > 3) + int(row['Q8'] > 3) + int(row['Q10'] > 3) + int(row['Q11'] > 3)

        # 2. Hyper

        # Conditions for Q12,Q16,Q18
        condition_5 = int(row['Q12'] > 2) + int(row['Q16'] > 2) + int(row['Q18'] > 2)

        # Conditions for Q5,Q6,Q13,Q14,Q15,Q17
        condition_6 = int(row['Q5'] > 3) + int(row['Q6'] > 3) + int(row['Q13'] > 3) + int(row['Q14'] > 3) + int(row['Q15'] > 3) + int(row['Q17'] > 3)

        # Calculate the final score of ADHD for the current row
        final_score = condition_1 + condition_2

        # Calculate the final score of ADD for the current row
        Inattention_score = condition_3 + condition_4

        # Calculate the final score of ADHD for the current row
        Hyperactivity_score = condition_5 + condition_6

        # Calculate the percentage for the current row
        final_percentage = (final_score / 18) * 100
        Inattention_percentage = (Inattention_score / 9) * 100
        Hyperactivity_percentage = (Hyperactivity_score / 9) * 100

        # Append the final score to the list
        Final_ADHD_scores.append(final_score)
        Inattention_scores.append(Inattention_score)
        Hyperactivity_scores.append(Hyperactivity_score)

        # Append the percentage for each line
        Final_ADHD_percentages.append(final_percentage)
        Inattention_percentages.append(Inattention_percentage)
        Hyperactivity_percentages.append(Hyperactivity_percentage)

    return final_percentage, Inattention_percentage, Hyperactivity_percentage

def compute_final_score_MANIA(data):
    # Initialize empty lists to store scores for each row
    Final_MANIA_scores_list = []
    Severity_MANIA_scores_list = []
    Final_MANIA_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 2 questions:
        # Conditions for Q22 and Q23
        condition_1 = int(row['Q22'] >= 2) + int(row['Q23'] >= 2)
        
        # Conditions for Q22 and Q23
        condition_2 = int(row['Q22']) + int(row['Q23'])
        
        # Calculate the final score of MANIA for the current row
        Final_MANIA_score = condition_2
        
        # Calculate the Severity score of MANIA for the current row
        Severity_MANIA_score = condition_1
        
        # Calculate the percentage for the current row
        Final_MANIA_percentage = (Final_MANIA_score / 8) * 100
        
        # Append the final score to the list
        Final_MANIA_scores_list.append(Final_MANIA_score)
        Severity_MANIA_scores_list.append(Severity_MANIA_score)
        
        # Append the percentage for each line
        Final_MANIA_percentage_list.append(Final_MANIA_percentage)
    
    return Final_MANIA_percentage

def compute_final_score_ANXIETY(data):
    # Initialize empty lists to store scores for each row
    Final_ANXIETY_scores_list = []
    Severity_ANXIETY_scores_list = []
    Final_ANXIETY_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 3 questions:
        # Conditions for Q24,Q25 and Q26
        condition_1 = int(row['Q24'] >= 2) + int(row['Q25'] >= 2) + int(row['Q26'] >= 2)
        
        # Conditions for Q24,Q25 and Q26
        condition_2 = int(row['Q24']) + int(row['Q25']) + int(row['Q26'])
        
        # Calculate the final score of Anxiety for the current row
        Final_ANXIETY_score = condition_2
        
        # Calculate the Severity score of Anxiety for the current row
        Severity_ANXIETY_score = condition_1
        
        # Calculate the percentage for the current row
        Final_ANXIETY_percentage = (Final_ANXIETY_score / 12) * 100
        
        # Append the final score to the list
        Final_ANXIETY_scores_list.append(Final_ANXIETY_score)
        Severity_ANXIETY_scores_list.append(Severity_ANXIETY_score)
        
        # Append the percentage for each line
        Final_ANXIETY_percentage_list.append(Final_ANXIETY_percentage)
    
    return Final_ANXIETY_percentage 

def compute_final_score_DEPRESSION(data):
    # Initialize empty lists to store scores for each row
    Final_DEPRESSION_scores_list = []
    Severity_DEPRESSION_scores_list = []
    Final_DEPRESSION_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 2 questions:
        # Conditions for Q19 and Q20
        condition_1 = int(row['Q19'] >= 2) + int(row['Q20'] >= 2)
        
        # Conditions for Q19 and Q20
        condition_2 = int(row['Q19']) + int(row['Q20'])
        
        # Calculate the final score of Depression for the current row
        Final_DEPRESSION_score = condition_2
        
        # Calculate the Severity score of Depression for the current row
        Severity_DEPRESSION_score = condition_1
        
        # Calculate the percentage for the current row
        Final_DEPRESSION_percentage = (Final_DEPRESSION_score / 8) * 100
        
        # Append the final score to the list
        Final_DEPRESSION_scores_list.append(Final_DEPRESSION_score)
        Severity_DEPRESSION_scores_list.append(Severity_DEPRESSION_score)
        
        # Append the percentage for each line
        Final_DEPRESSION_percentage_list.append(Final_DEPRESSION_percentage)
    
    return Final_DEPRESSION_percentage 

def compute_final_score_ANGER(data):
    # Initialize empty lists to store scores for each row
    Final_ANGER_scores_list = []
    Severity_ANGER_scores_list = []
    Final_ANGER_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q21
        condition_1 = int(row['Q21'] >= 2)
        
        # Conditions for Q21
        condition_2 = int(row['Q21'])
        
        # Calculate the final score of ANGER for the current row
        Final_ANGER_score = condition_2
        
        # Calculate the Severity score of ANGER for the current row
        Severity_ANGER_score = condition_1
        
        # Calculate the percentage for the current row
        Final_ANGER_percentage = (Final_ANGER_score / 4) * 100
        
        # Append the final score to the list
        Final_ANGER_scores_list.append(Final_ANGER_score)
        Severity_ANGER_scores_list.append(Severity_ANGER_score)
        
        # Append the percentage for each line
        Final_ANGER_percentage_list.append(Final_ANGER_percentage)
    
    return Final_ANGER_percentage

def compute_final_score_PSYCHOSIS(data):
    # Initialize empty lists to store scores for each row
    Final_PSYCHOSIS_scores_list = []
    Severity_PSYCHOSIS_scores_list = []
    Final_PSYCHOSIS_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 2 questions:
        # Conditions for Q30 and Q31
        condition_1 = int(row['Q31'] >= 1)+ int(row['Q30'] >= 1)
        
        # Conditions for Q30 and Q31
        condition_2 = int(row['Q31'])+ int(row['Q30'])
        
        # Calculate the final score of PSYCHOSIS for the current row
        Final_PSYCHOSIS_score = condition_2
        
        # Calculate the Severity score of PSYCHOSIS for the current row
        Severity_PSYCHOSIS_score = condition_1
        
        # Calculate the percentage for the current row
        Final_PSYCHOSIS_percentage = (Final_PSYCHOSIS_score / 8) * 100
        
        # Append the final score to the list
        Final_PSYCHOSIS_scores_list.append(Final_PSYCHOSIS_score)
        Severity_PSYCHOSIS_scores_list.append(Severity_PSYCHOSIS_score)
        
        # Append the percentage for each line
        Final_PSYCHOSIS_percentage_list.append(Final_PSYCHOSIS_percentage)
    
    return Final_PSYCHOSIS_percentage 

def compute_final_score_SOMATIC_SYMP(data):
    # Initialize empty lists to store scores for each row
    Final_SOMATIC_SYMP_scores_list = []
    Severity_SOMATIC_SYMP_scores_list = []
    Final_SOMATIC_SYMP_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 2 questions:
        # Conditions for Q27 and Q28
        condition_1 = int(row['Q27'] >= 2)+ int(row['Q28'] >= 2)
        
        # Conditions for Q27 and Q28
        condition_2 = int(row['Q27'])+ int(row['Q28'])
        
        # Calculate the final score of SOMATIC_SYMP for the current row
        Final_SOMATIC_SYMP_score = condition_2
        
        # Calculate the Severity score of SOMATIC_SYMP for the current row
        Severity_SOMATIC_SYMP_score = condition_1
        
        # Calculate the percentage for the current row
        Final_SOMATIC_SYMP_percentage = (Final_SOMATIC_SYMP_score / 8) * 100
        
        # Append the final score to the list
        Final_SOMATIC_SYMP_scores_list.append(Final_SOMATIC_SYMP_score)
        Severity_SOMATIC_SYMP_scores_list.append(Severity_SOMATIC_SYMP_score)
        
        # Append the percentage for each line
        Final_SOMATIC_SYMP_percentage_list.append(Final_SOMATIC_SYMP_percentage)
    
    return Final_SOMATIC_SYMP_percentage 

def compute_final_score_SUBSTANCE_USE(data):
    # Initialize empty lists to store scores for each row
    Final_SUBSTANCE_USE_scores_list = []
    Severity_SUBSTANCE_USE_scores_list = []
    Final_SUBSTANCE_USE_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 3 questions:
        # Conditions for Q33, Q34 and Q35 
        condition_1 = int(row['Q33'] >= 1)+ int(row['Q34'] >= 1) + int(row['Q35'] >= 1)
        
        # Conditions for Q33, Q34 and Q35
        condition_2 = int(row['Q33'])+ int(row['Q34']) + int(row['Q35'])
        
        # Calculate the final score of SUBSTANCE_USE for the current row
        Final_SUBSTANCE_USE_score = condition_2
        
        # Calculate the Severity score of SUBSTANCE_USE for the current row
        Severity_SUBSTANCE_USE_score = condition_1
        
        # Calculate the percentage for the current row
        Final_SUBSTANCE_USE_percentage = (Final_SUBSTANCE_USE_score / 12) * 100
        
        # Append the final score to the list
        Final_SUBSTANCE_USE_scores_list.append(Final_SUBSTANCE_USE_score)
        Severity_SUBSTANCE_USE_scores_list.append(Severity_SUBSTANCE_USE_score)
        
        # Append the percentage for each line
        Final_SUBSTANCE_USE_percentage_list.append(Final_SUBSTANCE_USE_percentage)
    
    return Final_SUBSTANCE_USE_percentage 

def compute_final_score_SUICIDAL(data):
    # Initialize empty lists to store scores for each row
    Final_SUICIDAL_scores_list = []
    Severity_SUICIDAL_scores_list = []
    Final_SUICIDAL_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q29 
        condition_1 = int(row['Q29'] >= 1)
        
        # Conditions for Q29
        condition_2 = int(row['Q29'])
        
        # Calculate the final score of SUICIDAL for the current row
        Final_SUICIDAL_score = condition_2
        
        # Calculate the Severity score of SUICIDAL for the current row
        Severity_SUICIDAL_score = condition_1
        
        # Calculate the percentage for the current row
        Final_SUICIDAL_percentage = (Final_SUICIDAL_score / 4) * 100
        
        # Append the final score to the list
        Final_SUICIDAL_scores_list.append(Final_SUICIDAL_score)
        Severity_SUICIDAL_scores_list.append(Severity_SUICIDAL_score)
        
        # Append the percentage for each line
        Final_SUICIDAL_percentage_list.append(Final_SUICIDAL_percentage)
    
    return Final_SUICIDAL_percentage 

def compute_final_score_DISSOCIATION(data):
    # Initialize empty lists to store scores for each row
    Final_DISSOCIATION_scores_list = []
    Severity_DISSOCIATION_scores_list = []
    Final_DISSOCIATION_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q32 
        condition_1 = int(row['Q32'] >= 2)
        
        # Conditions for Q32
        condition_2 = int(row['Q32'])
        
        # Calculate the final score of Dissociative for the current row
        Final_DISSOCIATION_score = condition_2
        
        # Calculate the Severity score of Dissociative for the current row
        Severity_DISSOCIATION_score = condition_1
        
        # Calculate the percentage for the current row
        Final_DISSOCIATION_percentage = (Final_DISSOCIATION_score / 4) * 100
        
        # Append the final score to the list
        Final_DISSOCIATION_scores_list.append(Final_DISSOCIATION_score)
        Severity_DISSOCIATION_scores_list.append(Severity_DISSOCIATION_score)
        
        # Append the percentage for each line
        Final_DISSOCIATION_percentage_list.append(Final_DISSOCIATION_percentage)

    
    return Final_DISSOCIATION_percentage 

def compute_final_score_Depression_SR(data):
    # Initialize empty lists to store scores for each row
    Final_Depression_SR_scores_list = []
    Final_Depression_SR_percentage_list = []
    Final_Depression_SR_sum_list = []
    
    for idx, row in data.iterrows():
        ## Scoring questions:
        # Conditions for QSR1,QSR2,QSR3 and QSR4  
        condition_1 = row[['QSR1', 'QSR2', 'QSR3', 'QSR4']].max()
        
        # Conditions for QSR6,QSR7,QSR8 and QSR9
        condition_2 = row[['QSR6', 'QSR7', 'QSR8', 'QSR9']].max()
        
        # Conditions for QSR15 and QSR16
        condition_3 = row[['QSR16', 'QSR15']].max()
        
        # Condition for the rest of the questions
        condition_4 = (row['QSR5'])+ (row['QSR10'])+ (row['QSR11'])+ (row['QSR12'])+ (row['QSR13']) + (row['QSR14'])
        
        # Sum of all questions scores
        condition_5 = (row['QSR1'])+ (row['QSR2'])+ (row['QSR3'])+(row['QSR4'])+ (row['QSR5'])+ (row['QSR6'])+(row['QSR7'])+(row['QSR8'])+ (row['QSR9'])+ (row['QSR10'])+ (row['QSR11'])+ (row['QSR12'])+ (row['QSR13'])+ (row['QSR14'])+ (row['QSR15'])+ (row['QSR16'])
                
        # Calculate the final score of Depression_SR for the current row
        Final_Depression_SR_score = condition_1 + condition_2 + condition_3 + condition_4
        Final_Depression_SR_sum = condition_5
        
        # Calculate the percentage for the current row
        Final_Depression_SR_percentage = (Final_Depression_SR_score / 27) * 100
        
        # Append the final score to the list
        Final_Depression_SR_scores_list.append(Final_Depression_SR_score)
        Final_Depression_SR_sum_list.append(Final_Depression_SR_sum)
        
        # Append the percentage for each line
        Final_Depression_SR_percentage_list.append(Final_Depression_SR_percentage)
    
    return Final_Depression_SR_percentage 





if __name__ == "__main__":
    # Load data
    test1_data = pd.read_csv("../pythonApi/dataset/Mental_health_dataset.csv")  
    test2_data = pd.read_csv("../pythonApi/dataset/Mental_health_dataset.csv")  
    test3_data = pd.read_csv("../pythonApi/dataset/QIDS_SR16.csv")  

    # Compute final scores using all functions

    # ADHD scores
    adhd_final, inattention, hyperactivity = compute_final_score_ADHD(test1_data)

    # Mania scores
    mania_final = compute_final_score_MANIA(test1_data)

    # Anxiety scores
    anxiety_final = compute_final_score_ANXIETY(test1_data)

    # Depression scores
    depression_final = compute_final_score_DEPRESSION(test1_data)

    # Anger scores
    anger_final = compute_final_score_ANGER(test1_data)

    # Psychosis scores
    psychosis_final = compute_final_score_PSYCHOSIS(test1_data)

    # Somatic symptom scores
    somatic_final = compute_final_score_SOMATIC_SYMP(test1_data)

    # Substance use scores
    substance_use_final = compute_final_score_SUBSTANCE_USE(test1_data)

    # Suicidal scores
    suicidal_final = compute_final_score_SUICIDAL(test1_data)

    # Dissociative scores
    dissociative_final = compute_final_score_DISSOCIATION(test1_data)

    # Depression SR scores
    depression_sr_final = compute_final_score_Depression_SR(test3_data)
    print("scikit-learn version:", sklearn.__version__)

    
# Load ADHD model
ADHD_BestModel_Oversampling = joblib.load("../pythonApi/models/ADHD_BestModel_Oversampling.sav")

# Load ANGER model
ANGER_BestModel_Oversampling = joblib.load("../pythonApi/models/ANGER_BestModel_Oversampling.sav")

# Load ANXIETY model
ANXIETY_BestModel_Oversampling = joblib.load("../pythonApi/models/ANXIETY_BestModel_Oversampling.sav")

# Load DEPRESSION model
DEPRESSION_BestModel_Oversampling = joblib.load("../pythonApi/models/DEPRESSION_BestModel_Oversampling.sav")

# Load DEP_QIDS16 model
DEP_QIDS16_BestModel_Oversampling = joblib.load("../pythonApi/models/DEP_QIDS16_BestModel_Oversampling.sav")

# Load DISSOCIATION model
DISSOCIATION_BestModel_Oversampling = joblib.load("../pythonApi/models/DISSOCIATION_BestModel_Oversampling.sav")

# Load MANIA model
MANIA_BestModel_Oversampling = joblib.load("../pythonApi/models/MANIA_BestModel_Oversampling.sav")

# Load PSYCHOSIS model
PSYCHOSIS_BestModel_Oversampling = joblib.load("../pythonApi/models/PSYCHOSIS_BestModel_Oversampling.sav")

# Load SOMATIC_SYMP model
SOMATIC_SYMP_BestModel_Oversampling = joblib.load("../pythonApi/models/SOMATIC_SYMP_BestModel_Oversampling.sav")

# Load SUBSTANCE_USE model
SUBSTANCE_USE_BestModel_Oversampling = joblib.load("../pythonApi/models/SUBSTANCE_USE_BestModel_Oversampling.sav")

# Load SUICIDAL model
SUICIDAL_BestModel_Oversampling = joblib.load("../pythonApi/models/SUICIDAL_BestModel_Oversampling.sav")


# SECTION 1: RESULTS

# For the test 1: Mental Health Assessment
print("These are the results of the test you've taken.")

# ADHD/ADD disorder
print("* ADHD/ADD disorder:")
print("   - Final attention-deficit/hyperactivity disorder percentage:", adhd_final)
print("   - Inattentive (ADD) symptoms percentage:", inattention)
print("   - Hyperactive-Impulsive(ADHD)symptoms percentage:", hyperactivity)

# Major Depressive Disorder
print("* Major Depressive Disorder:")
print("   - Final Depression percentage:", depression_final)

# Anxiety Disorder
print("* Anxiety Disorder:")
print("   - Final Anxiety percentage:", anxiety_final)

# Manic Episodes
print("* Manic Episodes:")
print("   - Final Mania percentage:", mania_final)

# Anger Episodes
print("* Anger Episodes:")
print("   - Final Anger percentage:", anger_final)

# Generalized Anxiety Disorder
print("* Generalized Anxiety Disorder:")
print("   - Final Mania percentage:", mania_final)

# Psychosis
print("* Psychosis:")
print("   - Final Psychosis percentage:", psychosis_final)

# Somatic symptoms
print("* Somatic symptoms:")
print("   - Final Somatic symptoms percentage:", somatic_final)

# Suicidal ideation
print("* Suicidal ideation:")
print("   - Final Suicidal ideation percentage:", suicidal_final)

# Dissociative Identity Disorder (DID)
print("* Dissociative Identity Disorder (DID):")
print("   - Dissociative Identity Disorder (DID) percentage:", dissociative_final)

# Substance Use Disorder
print("* Substance Use Disorder:")
print("   - Substance Use Disorder percentage:", substance_use_final)


# SECTION 2: Tentative Diagnosis

# For the test 1: Mental Health Assessment
print("\nThese are the results you'll show in this section according to the type of the test:")

# Get the model's prediction for each condition

# for ADHD
prediction_ADHD = ADHD_BestModel_Oversampling.predict(input_variables_ADHD)[0]
if prediction_ADHD == 0: 
    diag_ADHD = "You have Predominantly Inattentive (ADD) symptoms"
elif prediction_ADHD == 1: 
    diag_ADHD = "You have Predominantly Hyperactive-Impulsive(ADHD) symptoms"
elif prediction_ADHD == 2: 
    diag_ADHD = "You have Combined Inattentive and Hyperactive-Impulsive (ADHD) symptoms"
else: 
    diag_ADHD = "You have no ADHD nor ADD symptoms"

# for Depression
prediction_Dep = DEPRESSION_BestModel_Oversampling.predict(input_variables_Depression)[0]
if prediction_Dep == 0: 
    diag_Dep = "You are likely to be depressed"
else: 
    diag_Dep = "You are less likely to be depressed"

# for Dissociative Identity Disorder
prediction_did = DISSOCIATION_BestModel_Oversampling.predict(input_variables_DID)[0]
if prediction_did == 0: 
    diag_did = "You are likely showing high level of Dissociative Identity Disorder symptoms"
else: 
    diag_did = "You are not having Dissociative Identity Disorder symptoms"

# for Mania
prediction_mania = MANIA_BestModel_Oversampling.predict(input_variables_MANIA)[0]
if prediction_mania == 0: 
    diag_man = "You have likely a manic or hypomanic condition"
else: 
    diag_man = "You are less likely to be associated with significant symptoms of mania"

# for Anger
prediction_ang = ANGER_BestModel_Oversampling.predict(input_variables_ANGER)[0]
if prediction_ang == 0: 
    diag_ang = "You are likely to have anger issues"
else: 
    diag_ang = "You are less likely to be associated with significant symptoms of anger"

# for Anxiety
prediction_anx = ANXIETY_BestModel_Oversampling.predict(input_variables_Anxiety)[0]
if prediction_anx == 0: 
    diag_anx = "You have an elevated level of anxiety"
else: 
    diag_anx = "Your level of anxiety is not high"

# for Suicidal
prediction_suic = SUICIDAL_BestModel_Oversampling.predict(input_variables_SUICIDAL)[0]
if prediction_suic == 1: 
    diag_suic = "You are showing high level of suicidal ideation"
else: 
    diag_suic = "You are not having suicidal ideation"

# for Psychosis
prediction_psy = PSYCHOSIS_BestModel_Oversampling.predict(input_variables_PSYCHOSIS)[0]
if prediction_psy == 1: 
    diag_psy = "You are likely showing high level of psychosis symptoms"
else: 
    diag_psy = "You are not having psychosis symptoms"

# for Somatic
prediction_som = SOMATIC_SYMP_BestModel_Oversampling.predict(input_variables_SOMATIC)[0]
if prediction_som == 1: 
    diag_som = "You are likely showing high level of somatic symptoms"
else: 
    diag_som = "You are not having somatic symptoms"

# for Substance Use
prediction_sub = SUBSTANCE_USE_BestModel_Oversampling.predict(input_variables_SUBSTANCE_USE)[0]
if prediction_sub == 1: 
    diag_sub = "You are likely showing high level of substance use disorder symptoms"
else: 
    diag_sub = "You are not having substance use disorder symptoms"

# for DEPRESSION_QIDS_16 (SPECIFIC DEPRESSION TEST)
prediction_DEP_QIDS = DEP_QIDS16_BestModel_Oversampling.predict(input_variables_DEP_QIDS)[0]
if prediction_DEP_QIDS == 0: 
    diag_DEP_QIDS = "You have mild depression symptoms"
elif prediction_DEP_QIDS == 1: 
    diag_DEP_QIDS = "You have moderate depression symptoms"
elif prediction_DEP_QIDS == 2: 
    diag_DEP_QIDS = "You have no depression symptoms"
else: 
    diag_DEP_QIDS = "You have severe and very severe depression symptoms"

# Output the diagnosis based on the predictions for each condition

# For the test 1: Mental Health Assessment
print("# For the test 1: Mental Health Assessment")
print("   - Diagnosis for ADHD:", diag_ADHD)
print("   - Diagnosis for Depression:", diag_Dep)
print("   - Diagnosis for Dissociative Identity Disorder:", diag_did)
print("   - Diagnosis for Mania:", diag_man)
print("   - Diagnosis for Anger:", diag_ang)
print("   - Diagnosis for Anxiety:", diag_anx)
print("   - Diagnosis for Suicidal:", diag_suic)
print("   - Diagnosis for Psychosis:", diag_psy)
print("   - Diagnosis for Somatic symptoms:", diag_som)
print("   - Diagnosis for Substance Use Disorder:", diag_sub)

# Organize data into a dictionary
results1 = {
    "ADHD": {
        "Final_ADHD_percentage": adhd_final,
        "Inattention_percentage": inattention,
        "Hyperactivity_percentage": hyperactivity
    },
    "Mania": {
        "Final_Mania_percentage": mania_final
    },
    "Anxiety": {
        "Final_Anxiety_percentage": anxiety_final
    },
    "Depression": {
        "Final_Depression_percentage": depression_final
    },
    "Anger": {
        "Final_Anger_percentage": anger_final
    },
    "Psychosis": {
        "Final_Psychosis_percentage": psychosis_final
    },
    "Somatic_symptoms": {
        "Final_Somatic_symptoms_percentage": somatic_final
    },
    "Substance_Use": {
        "Final_Substance_Use_percentage": substance_use_final
    },
    "Suicidal": {
        "Final_Suicidal_percentage": suicidal_final
    },
    "Dissociation": {
        "Final_Dissociation_percentage": dissociative_final
    },
    "Depression_SR": {
        "Final_Depression_SR_percentage": depression_sr_final
    },
    "Mental Health Assessment": {
        "ADHD": diag_ADHD,
        "Depression": diag_Dep,
        "Dissociative Identity Disorder": diag_did,
        "Mania": diag_man,
        "Anger": diag_ang,
        "Anxiety": diag_anx,
        "Suicidal": diag_suic,
        "Psychosis": diag_psy,
        "Somatic symptoms": diag_som,
        "Substance Use Disorder": diag_sub
    },
}

# Write the dictionary into a JSON file
with open("../server/dataset_server/test1_results.json", "w") as json_file:
    json.dump(results1, json_file)

# For the test 2: ADHD/ADD
print("\n# For the test 2: ADHD/ADD")
print("   - Diagnosis for ADHD:", diag_ADHD)

results2 = {
    "ADHD/ADD": {
        "ADHD": diag_ADHD
    }
} 

# Write the dictionary into a JSON file
with open("../server/dataset_server/test2_results.json", "w") as json_file:
    json.dump(results2, json_file)


# For the test 3: Depression
print("\n# For the test 3: Depression")
print("   - Diagnosis for Depression:", diag_DEP_QIDS)

results3 = {
    "Depression": {
        "Depression": diag_DEP_QIDS
    }
} 

# Write the dictionary into a JSON file
with open("../server/dataset_server/test3_results.json", "w") as json_file:
    json.dump(results3, json_file)


