import unittest
from FileImportModule import *
from BST_Module import *

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
    	F = FileImport('Test1.txt')
        self.assertEqual(F.StoreFileArray(), ['hello'])

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
