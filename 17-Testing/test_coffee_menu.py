import unittest
from coffee_menu import CoffeeMenu

class TestCoffeeMenu(unittest.TestCase):
    def setUp(self):
        self.menu = CoffeeMenu()
    
    def tearDown(self):
        self.menu = None
    
    def test_get_price_existing_item(self):
        self.assertEqual(self.menu.get_price('latte'), 2.75)
    
    def test_get_price_non_existing_item(self):
        self.assertIsNone(self.menu.get_price("beans"))
    
    def test_add_item(self):
        self.menu.add_item('beans', 3.00)
        self.assertEqual(self.menu.get_price('beans'), 3.00)
    
if __name__ == '__main__':
    unittest.main()
    