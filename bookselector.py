import json
import random

json_file = open('eng-metadata.json','r')
json_data = json.load(json_file)
json_file.close()

booknum_dict = {}
for data in json_data:
    booknum_dict[data['txt_path']] = data['LoC_Class']

random_booknum_list = random.sample(booknum_dict.keys(),1000)
random_booknum_list.sort()
print(random_booknum_list)