
#---------------------------------------------------------
# <NAME>
# <EMAIL>
# Homework #2
# September 15, 2015
# test.py
# test
#---------------------------------------------------------

#!/usr/bin/env Python

from hw2.Oh.BST import *
from hw2.Oh import *
import re

def StoreFileArray(file_name):
    
    try:
        nums=open(file_name).read().split()
        
        for i in range(len(nums)):
            nums[i]=re.sub('\W',"",nums[i].lower())
            nums[i]=re.sub('\d',"",nums[i])
            nums[i]=re.sub('_',"",nums[i])
        nums=filter(None,nums)

    except IOError:
        print file_name, "can't be opened."
        raise SystemExit
    else:
        return nums
        
def MakeTree(nums):
    T=BSTree()
    for i in range(len(nums)):
        T.add(nums[i])
    #T.inOrderPrint()
    print "Elements in this tree: ", T.size()
    print "Depth of this tree: ", T.height()-1 
    
    
def MakeTree2(nums,word):
    T=BSTree()
    for i in range(len(nums)):
        T.add(nums[i])

    T.find(word)
    
from os.path import abspath               #Define file import


def main():  #Calling all the functions
   f_path = abspath(raw_input("Enter file name:"))
   F=StoreFileArray(f_path)
   
   while True:
        inputWord=str(raw_input("Query? :"))
        inputWord=inputWord.lower()
        if inputWord=="terminate":
            print "Goodbye!"
            break
        elif inputWord=="stats":
            MakeTree(F)
        else:
            print "The word",inputWord,"appears",
            MakeTree2(F,inputWord),
            print 'times in the tree'
           

main()  

raise SystemExit
