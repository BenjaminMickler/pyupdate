import json

def read_update_list(filename):
    with open(filename, 'r') as f:
        return json.load(f)