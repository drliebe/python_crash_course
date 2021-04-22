cats_filename = 'cats.txt'
dogs_filename = 'dogs.txt'

try:
    with open(cats_filename) as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    print('File not found.')

try:
    with open(dogs_filename) as file_object:
        contents = file_object.read()
        print(contents)
except FileNotFoundError:
    print('File not found.')

    