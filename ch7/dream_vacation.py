prompt = 'Where would you go on a dream vacation? '
prompt += "\n(enter 'quit' to stop): "

destinations = []

active = True
while active:
    destination = input(prompt)
    if destination == 'quit':
        active = False
    else:
        destinations.append(destination)

print('\nDestinations of a Dream Vacation:')
for destination in destinations:
    print(destination)