import json

filename = 'favorite_number.json'
prompt = 'Enter your favorite number: '
with open(filename, 'w') as file_object:
    favorite_number = input(prompt)
    json.dump(favorite_number, file_object)
    



