from json import JSONEncoder
from symptoms.models.symptom import BaseEntity


class EntityEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, BaseEntity):
            return obj.__dict__
        return JSONEncoder.default(self, obj)
