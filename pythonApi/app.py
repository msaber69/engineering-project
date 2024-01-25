from flask import Flask, render_template, request

app = Flask(__name__)

# ASRS-V1 Scoring Function
def score_asrs_v1(responses):
    inattentive_items = [1, 2, 3, 4, 7, 8, 9, 10, 11]
    hyperactive_motor_items = [5, 6, 12, 13, 14]
    hyperactive_verbal_items = [15, 16, 17, 18]

    inattentive_score = sum(responses[i] for i in inattentive_items if responses[i] > 2)
    hyperactive_motor_score = sum(responses[i] for i in hyperactive_motor_items if responses[i] > 3)
    hyperactive_verbal_score = sum(responses[i] for i in hyperactive_verbal_items if responses[i] > 3)

    return inattentive_score, hyperactive_motor_score, hyperactive_verbal_score

# DSM5-Adult Depression Scoring Function
def score_dsm5_adult_depression(responses):
    depression_items = [19, 20]

    depression_score = sum(responses[i] for i in depression_items)

    return depression_score

# Example route to handle ASRS-V1 form submission
@app.route('/asrs_v1', methods=['POST'])
def asrs_v1():
    if request.method == 'POST':
        # Assuming you have a form with input names corresponding to question numbers
        responses = {int(key): int(value) for key, value in request.form.items()}

        inattentive_score, hyperactive_motor_score, hyperactive_verbal_score = score_asrs_v1(responses)

        return render_template('asrs_result.html', inattentive=inattentive_score,
                               hyperactive_motor=hyperactive_motor_score, hyperactive_verbal=hyperactive_verbal_score)

# Example route to handle DSM5-Adult Depression form submission
@app.route('/dsm5_adult_depression', methods=['POST'])
def dsm5_adult_depression():
    if request.method == 'POST':
        # Assuming you have a form with input names corresponding to question numbers
        responses = {int(key): int(value) for key, value in request.form.items()}

        depression_score = score_dsm5_adult_depression(responses)

        return render_template('dsm5_adult_depression_result.html', depression=depression_score)

if __name__ == '__main__':
    app.run(debug=True)
