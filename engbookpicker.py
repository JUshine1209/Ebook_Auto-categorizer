import json

json_file = open('gutenberg-metadata.json')
json_data = json.load(json_file)
json_file.close()

comma_checker = 0

tmp_dict = {}
new_json_file = open('eng-metadata.json','w')
new_json_file.write('[')
for data in json_data:
    try:
        if data['Language'] == ['English'] and data['LoC Class'] and data['gd-num-padded'] and data['gd-path']:
            tmp_dict = {}
            tmp_dict['Language'] = data['Language']
            tmp_dict['LoC_Class'] = data['LoC Class']
            tmp_dict['txt_num'] = data['gd-num-padded']
            tmp_dict['txt_path'] = data['gd-path']
            new_json_file.write(json.dumps(tmp_dict))
            if comma_checker != len(json_data)-1:
                new_json_file.write(',')
                comma_checker += 1
        else:
            comma_checker += 1
            continue
    except:
        comma_checker += 1
        continue
    
new_json_file.write(']')
new_json_file.close()
