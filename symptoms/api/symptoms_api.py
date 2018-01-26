from flask import Blueprint, jsonify, request, Response
from symptoms.models.symptom import Diagnosis, Symptom

symptoms = Blueprint("symptoms", __name__)
diagnoses = Blueprint("diagnoses", __name__)


@symptoms.route("/", methods=['GET'])
def get_all_symptoms():
    return jsonify(Symptom.get_all())


@diagnoses.route("/", methods=['GET'])
def get_diagnoses_by_symptom():
    symptom_name = request.args.get("symptom")
    if not symptom_name:
        return Response(status=400)
    return jsonify(Diagnosis.get_all_by_symptom(symptom_name))


@diagnoses.route('/increment_weight', methods=['POST'])
def increment_weight():
    data = request.get_json()
    diagnosis_to_update = Diagnosis.get_one(data['symptom'], data['diagnosis'])
    diagnosis_to_update.weight += 1
    diagnosis_to_update.update()
    return Response(status=200)

