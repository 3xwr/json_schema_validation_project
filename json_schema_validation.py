import json
import jsonschema
import os

from jsonschema import validate

def validateJson(jsonData, testSchema):

    validator = jsonschema.Draft7Validator(testSchema)
    errors = validator.iter_errors(jsonData)
    
    for error in errors:
        error_msg = betterErrorMessages(str(error.message))
        readme_file.write(error_msg)
        readme_file.write('\n')

def betterErrorMessages(validation_error):
    '''
     Улучшение читаемости сообщений об ошибках для не разработчиков.
    '''
    if "is not of type 'null', 'integer'" in validation_error:
        validation_error = validation_error[:-len("is not of type 'null', 'integer'")]
        ret_msg = "ID of your object must be an integer, while it is currently " + validation_error
        return ret_msg
    if "is a required property" in validation_error:
        validation_error = validation_error[:-len("is a required property")]
        ret_msg = "Your object doesn't have the " + validation_error + "property, which is required by the corresponding schema"
        return ret_msg
    if "None is not of type 'object'" in validation_error:
        return "Found 'null' instead of your object"
    else:
        return validation_error

readme_file = open("readme.md", "w")

json_dir = 'event/'
schema_dir = 'schema/'

json_files = os.scandir(json_dir)

json_counter = 1


for json_file in json_files:

    schema_counter = 1
    my_json_file = open(json_dir + json_file.name)
    json_contents = json.loads(my_json_file.read())
    readme_file.write("\nLogs for JSON file #" + str(json_counter) + " (" + json_file.name +"):")
    print("\nWriting logs for JSON file #"+ str(json_counter) + " (" + json_file.name +"):")
    #print(json_contents)
    
    schema_files = os.scandir(schema_dir)
    for schema_file in schema_files:
        readme_file.write("\nTrying schema #" + str(schema_counter) + " (" + schema_file.name +")" +" for JSON file #" + str(json_counter) + ":" )
        readme_file.write('\n-------\n')
        print("\nTrying schema #" + str(schema_counter) + " (" + schema_file.name +")" +" for JSON file #" + str(json_counter))
        my_schema_file = open(schema_dir + schema_file.name)
        schema_contents = json.loads(my_schema_file.read())
        validateJson(json_contents, schema_contents)
        schema_counter += 1

        my_schema_file.close()
        
    readme_file.write('\n\n')
    print('------------')
    json_counter = json_counter+1
    my_json_file.close()


    