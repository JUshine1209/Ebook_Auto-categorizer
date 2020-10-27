import json
import random
import shutil

json_file = open('eng-metadata.json','r')
json_data = json.load(json_file)
json_file.close()

booknum_dict = {}
for data in json_data:
    booknum_dict[data['txt_path']] = data['LoC_Class']

booknum_list = list(booknum_dict.keys())
booknum_list.sort()

first_write = True
book_json = open('all_book.json','w')
book_json.write('[\n')
for book in booknum_list:
    shutil.copy('gutenberg-dammit-files/'+book,'randombooks')
    if first_write:
        first_write = False
    else :
        book_json.write(',\n')
    tmp_dict = {}
    tmp_dict['LoC_Class'] = booknum_dict[book][0][0]
    tmp_dict['txt_path'] = book
    book_json.write(json.dumps(tmp_dict))
book_json.write('\n]')
book_json.close()
