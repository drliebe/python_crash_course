filename = 'poll_responses.txt'
prompt = 'Why do you like programming? \n'

print("Enter 'q' to quit.")
with open(filename, 'w') as file_object:
    while True:
        reason = input(prompt)
        if reason == 'q':
            break
        else:
            file_object.write(reason + '\n')
    
