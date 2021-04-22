import json

filename = 'favorite_number.json'

try:
    with open(filename, 'r') as file_object:
        favorite_number = json.load(file_object)
        print('I remember you favorite number! It is ' 
              + str(favorite_number) + '.')
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as file_object:
        json.dump(favorite_number, file_object)
