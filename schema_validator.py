import json
import os

def is_valid_json(jsonData):
    try:
        json.loads(jsonData)
    except ValueError as err:
        return False
    return True

dir = 'schema/'

schemas = os.scandir(dir)
for schema in schemas:
    my_file = open(dir+schema.name)
    file_contents = my_file.read()
    checked_file = is_valid_json(file_contents)

    if(checked_file):
        print(my_file.name + ' is valid json')
    else:
        print(my_file.name + ' is not valid json')
