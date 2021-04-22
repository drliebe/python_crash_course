import unittest
from city_functions import formatted_city_country

class TestFormattedCityCountry(unittest.TestCase):

    def test_city_country(self):
        formatted_result = formatted_city_country('santiago', 'chile')
        self.assertEqual(formatted_result, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted_result = formatted_city_country('santiago', 'chile', 
            500000)
        self.assertEqual(formatted_result, 
                         'Santiago, Chile - population 500000')

unittest.main()