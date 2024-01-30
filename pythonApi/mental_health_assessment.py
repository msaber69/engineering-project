import joblib
from app import (
    adhd_final, inattention, hyperactivity, mania_final, anxiety_final, depression_final, anger_final, psychosis_final, somatic_final, substance_use_final, suicidal_final, dissociative_final, depression_sr_final, 
    input_variables_ADHD,
    input_variables_Depression,
    input_variables_DID,
    input_variables_MANIA,
    input_variables_ANGER,
    input_variables_Anxiety,
    input_variables_SUICIDAL,
    input_variables_PSYCHOSIS,
    input_variables_SOMATIC,
    input_variables_SUBSTANCE_USE,
    input_variables_DEP_QIDS
)

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

# For the test 2: ADHD/ADD
print("\n# For the test 2: ADHD/ADD")
print("   - Diagnosis for ADHD:", diag_ADHD)

# For the test 3: Depression
print("\n# For the test 3: Depression")
print("   - Diagnosis for Depression:", diag_DEP_QIDS)
