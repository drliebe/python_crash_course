prompt = 'Enter your age to find out the price of your ticket.'
prompt += "\n('quit' to stop): "

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    elif int(age) < 3:
        print('Your ticket is free.')
    elif int(age) < 12:
        print('Your ticket is $10.')
    else: 
        print('Your ticket is $15.')