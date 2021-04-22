cities = {
    'LA': {
        'county': 'Los Angeles',
        'population': 'Way Too Many',
        'fact': 'The beaches are nice.',
        },
    'Oakland': {
        'county': 'Alameda',
        'population': 'Too Many',
        'fact': 'The beaches are not nice.',
        },
    'Chicago': {
        'county': 'Cook',
        'population': 'fine if you are not there',
        'fact': 'totally not corrupt... totally.',
        },
    }

for city, city_info in cities.items():
    print(city + ':' + str(city_info))

print(cities)