def formatted_city_country(city, country, population=''):
    """Nicely format a city and country into a string."""
    if population:
        message = city.title() + ", " + country.title() + " - population "
        message += str(population)
    else:
        message = city.title() + ", " + country.title()
    return message

    