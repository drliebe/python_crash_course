favorite_numbers_dict = {
    'Josh': [42, 24],
    'Ryan': [12, 1],
    'Frank': [7],
    'Ted': [-100, 100],
    'Bill': [0],
}

for name, favorite_numbers in favorite_numbers_dict.items():
    print(name + "'s favorite numbers are:")
    for number in favorite_numbers:
        print('  ' + str(number))