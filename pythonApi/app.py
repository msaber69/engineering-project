import pandas as pd

# Similarly, import other DataFrames from CSV files
input_variables_ADHD = pd.read_csv("inputFiles/input_variables_ADHD.csv")
input_variables_Anxiety = pd.read_csv("inputFiles/input_variables_Anxiety.csv")
input_variables_MANIA = pd.read_csv("inputFiles/input_variables_MANIA.csv")
input_variables_ANGER = pd.read_csv("inputFiles/input_variables_ANGER.csv")
input_variables_PSYCHOSIS = pd.read_csv("inputFiles/input_variables_PSYCHOSIS.csv")
input_variables_SOMATIC = pd.read_csv("inputFiles/input_variables_SOMATIC.csv")
input_variables_SUBSTANCE_USE = pd.read_csv("inputFiles/input_variables_SUBSTANCE_USE.csv")
input_variables_SUICIDAL = pd.read_csv("inputFiles/input_variables_SUICIDAL.csv")
input_variables_DID = pd.read_csv("inputFiles/input_variables_DID.csv")
input_variables_Depression = pd.read_csv("inputFiles/input_variables_Depression.csv")
input_variables_DEP_QIDS = pd.read_csv("inputFiles/input_variables_DEP_QIDS.csv")


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
        condition_1 = (row['Q1'] > 2).astype(int) + (row['Q2'] > 2).astype(int) + (row['Q3'] > 2).astype(int) + (row['Q9'] > 2).astype(int) + (row['Q12'] > 2).astype(int) + (row['Q16'] > 2).astype(int) + (row['Q18'] > 2).astype(int)

        # Conditions for Q4, Q5, Q6, Q7, Q8, Q10, Q11, Q13, Q14, Q15, Q17
        condition_2 = (row['Q4'] > 3).astype(int) + (row['Q5'] > 3).astype(int) + (row['Q6'] > 3).astype(int) + (row['Q7'] > 3).astype(int) + (row['Q8'] > 3).astype(int) + (row['Q10'] > 3).astype(int) + (row['Q11'] > 3).astype(int) + (row['Q13'] > 3).astype(int) + (row['Q14'] > 3).astype(int) + (row['Q15'] > 3).astype(int) + (row['Q17'] > 3).astype(int)

        ## Differentiate between ADD (Inattention) and ADHD (Inattention+hyper):
        # 1. Inattention

        # Conditions for Q1,Q2,Q3,Q9
        condition_3 = (row['Q1'] > 2).astype(int) + (row['Q2'] > 2).astype(int) + (row['Q3'] > 2).astype(int) + (row['Q9'] > 2).astype(int)

        # Conditions for Q4,Q7,Q8,Q10,Q11
        condition_4 = (row['Q4'] > 3).astype(int) + (row['Q7'] > 3).astype(int) + (row['Q8'] > 3).astype(int) + (row['Q10'] > 3).astype(int) + (row['Q11'] > 3).astype(int)

        # 2. Hyper

        # Conditions for Q12,Q16,Q18
        condition_5 = (row['Q12'] > 2).astype(int) + (row['Q16'] > 2).astype(int) + (row['Q18'] > 2).astype(int)

        # Conditions for Q5,Q6,Q13,Q14,Q15,Q17
        condition_6 = (row['Q5'] > 3).astype(int) + (row['Q6'] > 3).astype(int) + (row['Q13'] > 3).astype(int) + (row['Q14'] > 3).astype(int) + (row['Q15'] > 3).astype(int) + (row['Q17'] > 3).astype(int)

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

    return Final_ADHD_percentages, Inattention_percentages, Hyperactivity_percentages

def compute_final_score_MANIA(data):
    # Initialize empty lists to store scores for each row
    Final_MANIA_scores_list = []
    Severity_MANIA_scores_list = []
    Final_MANIA_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 2 questions:
        # Conditions for Q22 and Q23
        condition_1 = (row['Q22'] >= 2).astype(int) + (row['Q23'] >= 2).astype(int) 
        
        # Conditions for Q22 and Q23
        condition_2 = (row['Q22']).astype(int) + (row['Q23']).astype(int) 
        
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
    
    return Final_MANIA_percentage_list

def compute_final_score_ANXIETY(data):
    # Initialize empty lists to store scores for each row
    Final_ANXIETY_scores_list = []
    Severity_ANXIETY_scores_list = []
    Final_ANXIETY_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 3 questions:
        # Conditions for Q24,Q25 and Q26
        condition_1 = (row['Q24'] >= 2).astype(int) + (row['Q25'] >= 2).astype(int) + (row['Q26'] >= 2).astype(int) 
        
        # Conditions for Q24,Q25 and Q26
        condition_2 = (row['Q24']).astype(int) + (row['Q25']).astype(int) + (row['Q26']).astype(int) 
        
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
    
    return Final_ANXIETY_percentage_list

def compute_final_score_DEPRESSION(data):
    # Initialize empty lists to store scores for each row
    Final_DEPRESSION_scores_list = []
    Severity_DEPRESSION_scores_list = []
    Final_DEPRESSION_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring the 2 questions:
        # Conditions for Q19 and Q20
        condition_1 = (row['Q19'] >= 2).astype(int) + (row['Q20'] >= 2).astype(int) 
        
        # Conditions for Q19 and Q20
        condition_2 = (row['Q19']).astype(int) + (row['Q20']).astype(int)
        
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
    
    return Final_DEPRESSION_percentage_list

def compute_final_score_ANGER(data):
    # Initialize empty lists to store scores for each row
    Final_ANGER_scores_list = []
    Severity_ANGER_scores_list = []
    Final_ANGER_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q21
        condition_1 = (row['Q21'] >= 2).astype(int)
        
        # Conditions for Q21
        condition_2 = (row['Q21']).astype(int) 
        
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
        condition_1 = (row['Q31'] >= 1).astype(int)+ (row['Q30'] >= 1).astype(int)
        
        # Conditions for Q30 and Q31
        condition_2 = (row['Q31']).astype(int)+ (row['Q30']).astype(int)
        
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
    
    return Final_PSYCHOSIS_percentage_list

def compute_final_score_SOMATIC_SYMP(data):
    # Initialize empty lists to store scores for each row
    Final_SOMATIC_SYMP_scores_list = []
    Severity_SOMATIC_SYMP_scores_list = []
    Final_SOMATIC_SYMP_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 2 questions:
        # Conditions for Q27 and Q28
        condition_1 = (row['Q27'] >= 2).astype(int)+ (row['Q28'] >= 2).astype(int)
        
        # Conditions for Q27 and Q28
        condition_2 = (row['Q27']).astype(int)+ (row['Q28']).astype(int)
        
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
    
    return Final_SOMATIC_SYMP_percentage_list

def compute_final_score_SUBSTANCE_USE(data):
    # Initialize empty lists to store scores for each row
    Final_SUBSTANCE_USE_scores_list = []
    Severity_SUBSTANCE_USE_scores_list = []
    Final_SUBSTANCE_USE_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 3 questions:
        # Conditions for Q33, Q34 and Q35 
        condition_1 = (row['Q33'] >= 1).astype(int)+ (row['Q34'] >= 1).astype(int) + (row['Q35'] >= 1).astype(int)
        
        # Conditions for Q33, Q34 and Q35
        condition_2 = (row['Q33']).astype(int)+ (row['Q34']).astype(int) + (row['Q35']).astype(int)
        
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
    
    return Final_SUBSTANCE_USE_percentage_list

def compute_final_score_SUICIDAL(data):
    # Initialize empty lists to store scores for each row
    Final_SUICIDAL_scores_list = []
    Severity_SUICIDAL_scores_list = []
    Final_SUICIDAL_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q29 
        condition_1 = (row['Q29'] >= 1).astype(int)
        
        # Conditions for Q29
        condition_2 = (row['Q29']).astype(int)
        
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
    
    return Final_SUICIDAL_percentage_list

def compute_final_score_DISSOCIATION(data):
    # Initialize empty lists to store scores for each row
    Final_DISSOCIATION_scores_list = []
    Severity_DISSOCIATION_scores_list = []
    Final_DISSOCIATION_percentage_list = []

    for idx, row in data.iterrows():
        ## Scoring 1 question:
        # Conditions for Q32 
        condition_1 = (row['Q32'] >= 2).astype(int)
        
        # Conditions for Q32
        condition_2 = (row['Q32']).astype(int)
        
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

    
    return Final_DISSOCIATION_percentage_list

def compute_final_score_Depression_SR(data):
    # Initialize empty lists to store scores for each row
    Final_Depression_SR_scores_list = []
    Final_Depression_SR_percentage_list = []
    Final_Depression_SR_sum_list = []
    
    for idx, row in data.iterrows():
        ## Scoring questions:
        # Conditions for QSR1,QSR2,QSR3 and QSR4  
        condition_1 = row[row[['QSR1', 'QSR2', 'QSR3', 'QSR4']].idxmax()]
        
        # Conditions for QSR6,QSR7,QSR8 and QSR9
        condition_2 = row[row[['QSR6', 'QSR7', 'QSR8', 'QSR9']].idxmax()]
        
        # Conditions for QSR15 and QSR16
        condition_3 = row[row[['QSR16', 'QSR15']].idxmax()]
        
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
    
    return Final_Depression_SR_percentage_list


if __name__ == "__main__":
    # Load data
    test1_data = pd.read_csv("dataset/Mental_health_dataset.csv")  
    test2_data = pd.read_csv("dataset/DATASET_ADHD.csv")  
    test3_data = pd.read_csv("dataset/QIDS_SR16.csv")  

    # Example usage of compute_final_score_ADHD
    adhd_final, inattention, hyperactivity = compute_final_score_ADHD(test1_data)
    print("ADHD Final Scores:", adhd_final)
    print("Inattention Scores:", inattention)
    print("Hyperactivity Scores:", hyperactivity)

    # Example usage of compute_final_score_MANIA
    mania_final = compute_final_score_MANIA(test2_data)
    print("Mania Final Scores:", mania_final)

    # Example usage of compute_final_score_Depression_SR
    depression_sr_final = compute_final_score_Depression_SR(test3_data)
    print("Depression_SR Final Scores:", depression_sr_final)
