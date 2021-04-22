import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee1 = Employee('Joshua', 'Love', 50000)
    
    def test_give_default_raise(self):
        self.employee1.give_raise()
        self.assertEqual(self.employee1.salary, 55000)

    def test_give_custom_raise(self):
        self.employee1.give_raise(10000)
        self.assertEqual(self.employee1.salary, 60000)

unittest.main()