import json

json_file = open('gutenberg-metadata.json')
json_data = json.load(json_file)
json_file.close()

first_write = True
tmp_dict = {}
new_json_file = open('eng-metadata.json','w')
new_json_file.write('[\n')
for data in json_data:
    try:
        if data['Language'] == ['English'] and data['LoC Class'] and data['gd-num-padded'] and data['gd-path']:
            if first_write:
                first_write = False
            else:
                new_json_file.write(',\n')
            tmp_dict = {}
            tmp_dict['LoC_Class'] = data['LoC Class']
            tmp_dict['txt_path'] = data['gd-path']
            new_json_file.write(json.dumps(tmp_dict))
        else:
            continue
    except:
        continue
    
new_json_file.write('\n]')
new_json_file.close()
