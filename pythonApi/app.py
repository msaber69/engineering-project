from flask import Flask, render_template, request
import pandas as pd
from joblib import load
from ANGER_BestModel_Oversampling import compute_final_score_ADHD

app = Flask(__name__)

# Load your dataset
data = pd.read_csv('DATASET_ADHD.csv')

# Load your models
adhd_model = load('ADHD_BestModel_Oversampling.sav')
anger_model = load('ANGER_BestModel_Oversampling.sav')
anxiety_model = load('ANXIETY_BestModel_Oversampling.sav')
# ... (repeat for other models)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        # Get user input or any other necessary data
        # ...

        # Call your scoring function for ADHD
        scored_data = compute_final_score_ADHD(data, adhd_model)

        # Extract relevant columns from the result
        result_data = scored_data[['Participant_ID', 'Final_ADHD_score', 'Inattention_scores', 'Hyperactivity_scores']]

        # Pass the result to the template
        return render_template('result.html', result=result_data.to_html())

if __name__ == '__main__':
    app.run(debug=True)
