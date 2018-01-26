import os
from symptoms.config import RESOURCES_DIR
from hashlib import md5

def get_resource_filename(filename):
    return os.path.join(RESOURCES_DIR, filename)


def open_resource_file(filename, mode):
    return open(os.path.join(RESOURCES_DIR, filename), mode)


def hash_key(key):
    key = key.encode('utf-8')
    return md5(key).hexdigest()