files = ['frankenstein.txt', 'pride_and_prejudice.txt']

for file in files:
    try:
        with open(file) as file_object:
            contents = file_object.read()
    except:
        print('File does not exist.')
    else:
        the_count = contents.lower().count('the')
        print("The word 'the' appears " + str(the_count) + 
              " times in " + file + ".")
