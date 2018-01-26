import glob, pickle
from abc import ABC, abstractmethod
from symptoms import utils


class BaseEntity(ABC):

    @staticmethod
    @abstractmethod
    def get_all():
        pass

    @staticmethod
    @abstractmethod
    def get_one(*args, **kwargs):
        pass


    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Symptom(BaseEntity):

    def __init__(self, symptom_name:str=None):
        self.symptom_name = symptom_name

    @staticmethod
    def get_all():
        all_symptoms = []

        for filename in glob.glob(utils.get_resource_filename("symptom_*")):
            with open(filename, 'rb') as symptoms_resource:
                all_symptoms.append(pickle.load(symptoms_resource))
        return all_symptoms

    @staticmethod
    def get_one(symptom_name):

        filename = utils.get_resource_filename(
            f"symptom_{utils.hash_key(symptom_name)}")

        with open(filename, 'rb') as symptoms_resource:
            return Symptom(**pickle.load(symptoms_resource))


class Diagnosis(BaseEntity):

    def __init__(self, diagnosis_name: str = None,
                 corresponding_symptom: str = None, weight=0):
        self.diagnosis_name = diagnosis_name
        self.corresponding_symptom = corresponding_symptom
        self.weight = weight

    @staticmethod
    def get_all():
        all_diagnoses = []

        for filename in glob.glob(utils.get_resource_filename("diagnosis_*")):
            with open(filename, 'rb') as diagnosis_resource:
                all_diagnoses.append(pickle.load(diagnosis_resource))
        return all_diagnoses

    @staticmethod
    def get_one(symptom_name, diagnosis_name):
        filename = utils.get_resource_filename(
            f"diagnosis_{utils.hash_key(diagnosis_name)}_{utils.hash_key(symptom_name)}")

        with open(filename, 'rb') as diagnosis_resource:
            return Diagnosis(**pickle.load(diagnosis_resource))

    def update(self):
        filename = utils.get_resource_filename(
            f"diagnosis_{utils.hash_key(self.diagnosis_name)}_{utils.hash_key(self.corresponding_symptom)}")
        with open(filename, 'wb') as diagnosis_resource:
            pickle.dump(self.__dict__, diagnosis_resource)

    @staticmethod
    def get_all_by_symptom(symptom_name):
        all_diagnoses = []

        for filename in glob.glob(utils.get_resource_filename(
                f"diagnosis_*_{utils.hash_key(symptom_name)}")):
            with open(filename, 'rb') as diagnosis_resource:
                all_diagnoses.append(pickle.load(diagnosis_resource))
        return all_diagnoses
