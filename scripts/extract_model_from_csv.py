import csv
import os
from symptoms.config import RESOURCES_DIR
from symptoms.models.symptom import Diagnosis, Symptom
from symptoms import utils
import pickle

symptoms_and_diagnoses = {}


def save_resource_object(resource_object, filename):
    with open(os.path.join(RESOURCES_DIR, filename), 'wb') as save_file:
        pickle.dump(resource_object, save_file)


def extract_all_symptoms():
    with open(os.path.join(RESOURCES_DIR, 'symptoms.csv'), 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            row = [x.strip() for x in row]
            symptoms_and_diagnoses[row[0]] = row[1:]
    symptoms_cache = []
    diagnoses_cache = []
    for symptom, diagnoses in symptoms_and_diagnoses.items():
        new_symptom = Symptom(symptom_name=symptom)
        symptoms_cache.append(new_symptom)
        save_resource_object(new_symptom, f"symptom_{utils.hash_key(symptom)}")
        for diagnosis in diagnoses:
            new_diagnosis = Diagnosis(diagnosis_name=diagnosis,
                                      corresponding_symptom=symptom)
            diagnoses_cache.append(new_diagnosis)
            save_resource_object(
                new_diagnosis,
                f"diagnosis_{utils.hash_key(diagnosis)}_{utils.hash_key(symptom)}")

    return symptoms_cache, diagnoses_cache


if __name__ == '__main__':
    extract_all_symptoms()
