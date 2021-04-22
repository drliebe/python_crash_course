prompt = 'Please enter your requested pizza topings.'
prompt += "\nEnter 'quit' to stop. "

active = True
while active:
    topping_requested = input(prompt)
    if topping_requested == 'quit':
        active = False
    else:
        print('We will add ' + topping_requested + ' to your pizza!')
