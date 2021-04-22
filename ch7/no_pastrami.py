sandwich_orders = ['salami', 'pastrami', 'pastrami', 'ham',
                   'pastrami', 'tuna', 'chicken']
finished_sandwiches = []

print('We have run out of pastrami.')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your ' + sandwich + ' sandwich.')
    finished_sandwiches.append(sandwich)

print('\nToday we made the following sandwiches:')
for sandwich in finished_sandwiches:
    print(sandwich)