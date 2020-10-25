import json
import random

json_file = open('eng-metadata.json','r')
json_data = json.load(json_file)
json_file.close()

booknum_list = []
for data in json_data:
    booknum_list.append(data['txt_path'])

random_booknum_list = random.sample(booknum_list,1000)
random_booknum_list.sort()
print(random_booknum_list)
print(len(random_booknum_list))