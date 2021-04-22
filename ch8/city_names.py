def city_country(city_name, country):
    formatted_string = city_name.title() + ', ' + country.title()
    return formatted_string

print(city_country('Dallas', 'the United States of America'))
print(city_country('Vancouver', 'Canada'))
print(city_country('Tijuana', 'Mexico'))