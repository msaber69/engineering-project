# app.py
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
from joblib import load

app = Flask(__name__)
api = Api(app)

# Load models
adhd_model = load('models/ADHD_BestModel_Oversampling.sav')
anger_model = load('models/ANGER_BestModel_Oversampling.sav')
anxiety_model = load('models/ANXIETY_BestModel_Oversampling.sav')
dep_qids16_model = load('models/DEP_QIDS16_BestModel_Oversampling.sav')
depression_model = load('models/DEPRESSION_BestModel_Oversampling.sav')
dissociation_model = load('models/DISSOCIATION_BestModel_Oversampling.sav')
mania_model = load('models/MANIA_BestModel_Oversampling.sav')
psychosis_model = load('models/PSYCHOSIS_BestModel_Oversampling.sav')
somatic_symp_model = load('models/SOMATIC_SYMP_BestModel_Oversampling.sav')
substance_use_model = load('models/SUBSTANCE_USE_BestModel_Oversampling.sav')
suicidal_model = load('models/SUICIDAL_BestModel_Oversampling.sav')

class PredictADHD(Resource):
    def post(self):
        try:
            data = request.json  # Assuming JSON data
            prediction = adhd_model.predict(data['input_data'])
            return jsonify({'prediction': prediction.tolist()})
        except Exception as e:
            return jsonify({'error': str(e)})

api.add_resource(PredictADHD, '/predict_adhd')

if __name__ == '__main__':
    app.run(debug=True)
