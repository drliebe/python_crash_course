import json

filename = 'favorite_number.json'
with open(filename, 'r') as file_object:
    favorite_number = json.load(file_object)
    print(favorite_number)