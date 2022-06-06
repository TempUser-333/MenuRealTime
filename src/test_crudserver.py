import unittest
from unittest import TestCase
import requests
from logger_files.test_custom_logger import logger


class TestCRUDServer(TestCase):
    def test_get_all_the_categories_in_the_menu(self):
        logger.info('test-1 started')
        
        res = requests.get('http://127.0.0.1:8000/get/all/the/categories/in/the/menu/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find('Appetizers')) == True)
        self.assertTrue(bool(~res_1.find('Beverages')) == True)
        self.assertTrue(bool(~res_1.find('Entrees')) == True)
        self.assertTrue(bool(~res_1.find('Desserts')) == True)
        self.assertFalse(bool(~res_1.find('DRINKS')) == False)
        self.assertFalse(bool(~res_1.find('FOOD')) == False)
        self.assertEqual(bool(~res_1.find('PIZZA')), True)
        
        logger.info('test-1 ended')
        
    def test_check_for_the_presence_of_menuitems_in_the_categories(self):
        logger.info('test-2 started')
        
        res = requests.get('http://127.0.0.1:8000/check/for/the/presence/of/menuitems/in/the/categories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Appetizers': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Beverages': 'ABSENT'")) == True)
        self.assertTrue(bool(~res_1.find("'FISH': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Catering': 'ABSENT'")) == True)
        self.assertFalse(bool(~res_1.find("'Oxford Menu': 'ABSENT'")) == False)
        self.assertFalse(bool(~res_1.find("'Desserts': 'PRESENT'")) == False)
        self.assertEqual(bool(~res_1.find("'PIZZA': 'ABSENT'")), True)
        
        logger.info('test-2 ended')
        
    def test_get_menuitems_in_categories(self):
        logger.info('test-3 started')
        
        res = requests.get('http://127.0.0.1:8000/get/menuitems/in/the/categories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Appetizers': ['Blooming Onion'")) == True)
        self.assertTrue(bool(~res_1.find("'FISH': ['Chili Cup']")) == True)
        self.assertTrue(bool(~res_1.find("'Oxford Menu': 'No menuItems present'")) == True)
        self.assertTrue(bool(~res_1.find("'PIZZA': 'No menuItems present'")) == True)
        self.assertFalse(bool(~res_1.find("'DRINKS': 'No menuItems present'")) == False)
        self.assertFalse(bool(~res_1.find("'Entrees': 'No menuItems present'")) == False)
        self.assertEqual(bool(~res_1.find("'Beverages': 'No menuItems present'")), True)
        
        logger.info('test-3 ended')
        
        
    def test_get_menuitems_in_the_categories(self):
        logger.info('test-4 started')
        
        res = requests.get('http://127.0.0.1:8000/check/for/subcategories/in/the/categories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Appetizers': 'ABSENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Beverages': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'FISH': 'ABSENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Catering': 'ABSENT'")) == True)
        self.assertFalse(bool(~res_1.find("'PIZZA': 'ABSENT'")) == False)
        self.assertFalse(bool(~res_1.find("'DRINKS': 'PRESENT'")) == False)
        self.assertEqual(bool(~res_1.find("'Oxford Menu': 'PRESENT'")), True)
        
        logger.info('test-4 ended')
        
    def test_get_subcategories_in_the_categories(self):
        logger.info('test-5 started')
        
        res = requests.get('http://127.0.0.1:8000/get/subcategories/in/the/categories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Appetizers': 'No subcategories present'")) == True)
        self.assertTrue(bool(~res_1.find("'Beverages': ['Non Alcoholic Beverages']")) == True)
        self.assertTrue(bool(~res_1.find("'FISH': 'No subcategories present'")) == True)
        self.assertTrue(bool(~res_1.find("'DRINKS': ['Whiskey/Bourbon']")) == True)
        self.assertFalse(bool(~res_1.find("'Catering': 'No subcategories present'")) == False)
        self.assertFalse(bool(~res_1.find("'PIZZA': 'No subcategories present'")) == False)
        self.assertEqual(bool(~res_1.find("'Entrees': ['Combos'")), True)
        
        logger.info('test-5 ended')
        
        
    def test_check_for_menuitems_in_subcategories(self):
        logger.info('test-6 started')
        
        res = requests.get('http://127.0.0.1:8000/check/for/menuitems/in/the/subcategories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Non Alcoholic Beverages': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Combos': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Pasta': 'PRESENT'")) == True)
        self.assertTrue(bool(~res_1.find("'Whiskey/Bourbon': 'ABSENT'")) == True)
        self.assertFalse(bool(~res_1.find("'Oxford Classics': 'PRESENT'")) == False)
        self.assertFalse(bool(~res_1.find("'Pizza': 'PRESENT'")) == False)
        self.assertEqual(bool(~res_1.find("'Steaks': 'PRESENT'")), True)
        
        logger.info('test-6 ended')
        
    def test_get_menuitems_in_the_subcatgories(self):
        logger.info('test-7 started')
        
        res = requests.get('http://127.0.0.1:8000/get/menuitems/in/the/subcategories/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Whiskey/Bourbon': 'No menuitems present'")) == True)
        self.assertTrue(bool(~res_1.find("'Non Alcoholic Beverages': ['Brisk Iced Tea'")) == True)
        self.assertTrue(bool(~res_1.find("'Combos': ['Date Night Combo']")) == True)
        self.assertTrue(bool(~res_1.find("'Pasta': ['Create Your Own Pasta'")) == True)
        self.assertFalse(bool(~res_1.find("'Seafood': ['D - Baked Shrimp'")) == False)
        self.assertFalse(bool(~res_1.find("'Oxford Classics': ['Chicken Pot Pie with Vegetables'")) == False)
        self.assertEqual(bool(~res_1.find("'Pizza': ['Build Your Own Pizza'")), True)
        
        logger.info('test-7 ended')
        
    def test_get_overview_of_entire_menu(self):
        logger.info('test-8 started')
        
        res = requests.get('http://127.0.0.1:8000/get/overview/of/the/entire/menu/')
        res_1 = res.text
        
        self.assertTrue(bool(~res_1.find("'Appetizers': [{'CATEGORIES': ['Blooming Onion'")) == True)
        self.assertTrue(bool(~res_1.find("'Salads & Soups': [{'CATEGORIES': ['Apple Cran Salad'")) == True)
        self.assertTrue(bool(~res_1.find("'FISH': [{'CATEGORIES': ['Chili Cup'")) == True)
        self.assertTrue(bool(~res_1.find("'PIZZA': [{'CATEGORIES': 'No categories present'")) == True)
        self.assertFalse(bool(~res_1.find("'DRINKS': [{'CATEGORIES': 'No categories present'")) == False)
        self.assertFalse(bool(~res_1.find("'Oxford Menu': [{'CATEGORIES': 'No categories present'")) == False)
        self.assertEqual(bool(~res_1.find("'Desserts': [{'CATEGORIES': ['Carrot Cake'")), True)
        
        logger.info('test-8 ended')
        
        
    
if __name__ == '__main__':
    unittest.main()
