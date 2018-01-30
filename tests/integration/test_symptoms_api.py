from urllib import parse
from symptoms.models.symptom import Diagnosis
from scripts.extract_model_from_csv import extract_all_symptoms


def test_get_all_symptoms(testapp):
    symptoms, _ = extract_all_symptoms()
    response = testapp.get('/symptoms/')

    response_json = sorted(response.json, key=lambda x: x['symptom_name'])

    actual_data = sorted([x.__dict__ for x in symptoms],
                         key=lambda x: x['symptom_name'])

    assert(response_json == actual_data)


def test_get_diagnoses_by_symptom(testapp):
    url_encoded_symptom = "runny%20nose"
    response = testapp.get(f'/diagnoses/?symptom={url_encoded_symptom}')
    for diagnosis in response.json:
        assert diagnosis['corresponding_symptom'] == 'runny nose'
    pass


def test_get_top_diagnosis(testapp):
    testapp.post('/diagnoses/reset_weights')
    test_payload = {'symptom': 'runny nose', 'diagnosis': 'common cold'}
    testapp.post_json('/diagnoses/increment_weight', test_payload)
    response = testapp.get(
        '/diagnoses/top_diagnosis?symptom='
        f'{parse.quote(test_payload["symptom"])}')
    print(response)
    assert response.json['diagnosis_name'] == test_payload['diagnosis']


def test_increment_weight(testapp):
    testapp.post('/diagnoses/reset_weights')
    test_payload = {'symptom': 'runny nose', 'diagnosis': 'common cold'}
    testapp.post_json('/diagnoses/increment_weight', test_payload)
    diagnosis_in_question = Diagnosis.get_one(test_payload['symptom'],
                                              test_payload['diagnosis'])
    assert diagnosis_in_question.weight == 1


def test_reset_weight(testapp):
    testapp.post('/diagnoses/reset_weights')
    diagnoses = Diagnosis.get_all()
    for diagnosis in diagnoses:
        assert(diagnosis.weight == 0)