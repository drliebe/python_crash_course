sandwich_orders = ['salami', 'ham', 'tuna', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich.')
    finished_sandwiches.append(sandwich)

print('\nToday we made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich)