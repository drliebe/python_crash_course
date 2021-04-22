number_input = input('Enter a number:\n')
number_input = int(number_input)
if number_input % 10 == 0:
    print('Great! ' + str(number_input) + ' is a multiple of 10.')
else:
        print('Terrible! ' + str(number_input) 
              + ' is not a multiple of 10.')
