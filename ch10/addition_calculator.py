prompt1 = "Enter the first number to be added: "
prompt2 = "Enter the second number to be added: "

print("Enter 'q' to quit.")
while True:
    number1 = input(prompt1)
    if number1 == 'q':
        break
    number2 = input(prompt2)
    if number2 == 'q':
        break

    try:
        sum = int(number1) + int(number2)
    except ValueError:
        print('Please enter integers.')
    else:
        print('The sum is: ' + str(sum) + '.')
