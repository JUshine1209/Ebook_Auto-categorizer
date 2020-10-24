import json

json_file = open('eng-metadata.json','r')
json_data = json.load(json_file)
json_file.close()

for data in json_data:
    pass