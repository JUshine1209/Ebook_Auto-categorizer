import json
import random
import shutil

json_file = open('eng-metadata.json','r')
json_data = json.load(json_file)
json_file.close()

booknum_dict = {}
for data in json_data:
    booknum_dict[data['txt_path']] = data['LoC_Class']

random_booknum_list = random.sample(booknum_dict.keys(),1000)
random_booknum_list.sort()
print(random_booknum_list)

first_write = True
random_book_json = open('random_book.json','w')
for book in random_booknum_list:
    shutil.copy('gutenberg-dammit-files/'+book,'randombooks')
    if first_write:
        first_write = False
    else :
        random_book_json.write(',\n')
    tmp_dict = {}
    tmp_dict['LoC_Class'] = booknum_dict[book]
    tmp_dict['txt_path'] = book
    random_book_json.write(json.dumps(tmp_dict))

