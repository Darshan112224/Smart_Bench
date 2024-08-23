import json

with open('./enter_data/student_data.json', mode='r') as f:
    # At first, read the JSON file and store its content in an Python variable
    # By using json.load() function

    json_data = json.load(f)

    # So now json_data contains list of dictionaries
    # (because every JSON is a valid Python dictionary)

# Then we create a result list, in which we will store our names
result_list = []

# We start to iterate over each dictionary in our list
for json_dict in json_data:
    # We append each name value to our result list
    result_list.append(json_dict['Name'])

print(result_list)  # ['Hurzuf', 'Novinki']
