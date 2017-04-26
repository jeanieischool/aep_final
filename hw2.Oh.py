#---------------------------------------------------------
# <NAME>
# <EMAIL>
# Homework #2
# September 15, 2015
# hw2.py
# Main
#---------------------------------------------------------
from os.path import abspath               #Define file import
from BST_Module import *
import re

def StoreFileArray(file_name):
    
    try:
        nums=open(file_name).read().split()
        
        for i in range(len(nums)):
            nums[i]=re.sub('\W',"",nums[i].lower())
            nums[i]=re.sub('\d',"",nums[i]) #I didn't realize this doesn't capture "_" for some reason
            #I didn't realize that this loop does not remove empty elements
        

    except IOError:
        print file_name, "can't be opened." #This did not work right"
    else:
        return nums

def main(nums):
    T = BSTree()
    for i in range(len(nums)):
        T.add(nums[i])
    # Functions for use
    # T.find(word)
    # T.find(word)
    # T.size()
    print T.height()
    # print T.inOrderPrint()
 
    


if __name__ == "__main__":
    f_path = abspath(raw_input("Enter file name:"))
	F=StoreFileArray(f_path)
    main(F)  

