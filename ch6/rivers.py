rivers = {
    'mississippi': 'united states of america',
    'amazon': 'brazil',
    'nile': 'egypt',
}

for river, country in rivers.items():
    print('The ' + river.title() + 
          ' river runs through ' + country.title() + '.')

for river in rivers.keys():
    print('The ' + river.title() + ' is a river.')

for country in rivers.values():
    print(country.title() + ' is a country.')