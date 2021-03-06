import unittest
from FileImportModule import *
from BST_Module import *
import itertools

class TestFileImportAndBinarySearchTree(unittest.TestCase):

    def test_fileRead(self):
    	F = FileImport('test1.txt')
        self.assertEqual(F.StoreFileArray(), ['hello'])

    def test_errorHandling(self):
        F = FileImport('test1.txtffddde')
        self.assertEqual(F.StoreFileArray(), 'No such file')

    def test_textSanitation(self):
        F = FileImport('test2.txt')
        self.assertEqual(F.StoreFileArray(), ['hello', 'i', 'think', "you're", 'a', 'sister-in-law'])

    def test_removeEmpty(self):
        F = FileImport('test3.txt')
        self.assertEqual(F.StoreFileArray(), ['hello', 'i', 'think', "you're", 'a', 'sister-in-law'])

    def test_constructTree(self):
        F = FileImport('test4.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
            
        orderlist = T.inOrderPrint()

        printlist = [orderlist[0], orderlist[1][0]]
        self.assertEqual(printlist, ['who', "are"])

    def test_inOrderTree(self):
        F = FileImport('test4.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
            
        orderlist = T.inOrderPrint()

        printlist = [orderlist[0], orderlist[1][0], orderlist[1][2][0], orderlist[1][2][2][0], orderlist[1][2][2][2][0], orderlist[2][0], orderlist[2][1][0], orderlist[2][1][2][0], orderlist[2][2][0]]
        self.assertEqual(printlist, ['who', "are", 'one', 'tar', 'the', 'you', "yes", 'yo', 'zoo'])

    def test_checkSize(self):
        F = FileImport('test5.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
        
        size = T.size()
        self.assertEqual(size, 9)  



    def test_checkHeight(self):
        F = FileImport('test5.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
        
        size = T.height()
        self.assertEqual(size, 4)  

    def test_wordCount(self):
        F = FileImport('test5.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
        
        count = T.find('yo')
        self.assertEqual(count[0][0][0][0], 3)  

    def test_inReverseTree(self):
        F = FileImport('test4.txt')
        nums=F.StoreFileArray()
        T = BSTree()
        for i in range(len(nums)):
            T.add(nums[i])
            
        orderlist = T.inOrderPrint()

        printlist = [orderlist[0], orderlist[2][0], orderlist[2][1][0], orderlist[2][1][2][0], orderlist[2][2][0], orderlist[1][0], orderlist[1][2][0], orderlist[1][2][2][0], orderlist[1][2][2][2][0]]
        self.assertEqual(printlist, ['who', 'you', "yes", 'yo', 'zoo', 'are', 'one', 'tar', 'the', ])


    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()
