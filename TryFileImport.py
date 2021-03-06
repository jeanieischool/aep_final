# -*- coding: utf-8-sig -*-
#---------------------------------------------------------
# <NAME>
# <EMAIL>
# Homework #2
# September 15, 2015
# BST.py
# BST
#---------------------------------------------------------
from FileImportModule import *
import itertools
import re

class Node:
    #Constructor Node() creates node
    def __init__(self,word):
        self.word = word
        self.right = None
        self.left = None
        self.count = 1

class BSTree:
    #Constructor BSTree() creates empty tree
    def __init__(self, root=None):
        self.root = root
        
    #Add node to tree with word
    def add(self, word):
        if not self.root:
            self.root = Node(word)
            return
        _add(self.root, word)
    
    #Find word in tree
    def find(self, word):
        return _find(self.root, word)

    #Print in order entire tree
    def inOrderPrint(self):
        return _inOrderPrint(self.root)

    def size(self):
        return _size(self.root)

    def height(self):
        return _height(self.root)

#Function to add node with word as word attribute
def _add(root, word):
    if root.word == word:
        root.count +=1
        return root.count
    if root.word > word:
        if root.left == None:
            root.left = Node(word)
        else:
            _add(root.left, word)
    else:
        if root.right == None:
            root.right = Node(word)
        else:
            _add(root.right, word)

#Function to find word
def _find(root, word):
    if not root:
        return 0
    if root.word == word:
        flist=[root.count]
        return flist
    elif root.word > word:
        if root.left == None:
            return 0
        else:
            flist=[_find(root.left, word)]
            return flist
    else:
        if root.right == None:
            return 0
        else:
            flist=[_find(root.right, word)]
            return flist

#Get size of tree
def _size(root):
    if not root:
        return 0
    else:
        return 1+ _size(root.right) + _size(root.left)
        

#Get height of tree
def _height(root):
    if not root:
        return 0
    elif root.right==None and root.left==None:
        return 0
    else:
        return 1+max(_height(root.left),_height(root.right))
    

#Function to print tree in order
def _inOrderPrint(root):
    if not root:
        return
    jlist = [root.word]
    # jlist.append(root.word)
    # print root.word
    # print root.count
    # _inOrderPrint(root.left)
    
    jlist.append(_inOrderPrint(root.left))
    jlist.append(_inOrderPrint(root.right))
    # _inOrderPrint(root.right)
    # jlist.append(_inOrderPrint(root.right))
    return jlist


F = FileImport('test5.txt')
nums=F.StoreFileArray()
T = BSTree()
for i in range(len(nums)):
    T.add(nums[i])
john=T.find('yo')



# my_list = re.sub('\d',"",john[0])
print john[0][0][0][0]



# orderlist = T.inOrderPrint()
# s=filter(None, printlist)
# s=[x for x in printlist if x=='None']
# print printlist


# print orderlist[0]
# print orderlist[1][0], orderlist[1][2][0], orderlist[1][2][2][0], orderlist[1][2][2][2][0]
# print orderlist[2][0], orderlist[2][1][0], orderlist[2][1][2][0], orderlist[2][2][0]

# outputlist=[]
# for values in printlist:
#     outputlist.append(values[0])

# print(outputlist) 

# testlist = []
# testlist = itertools.repeat(printlist, 5)
# print testlist


