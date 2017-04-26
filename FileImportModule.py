#FileImport

from os.path import abspath   
import re

class FileImport:
	def __init__(self):
		self.path = abspath(raw_input("Enter file name:"))

	def StoreFileArray(self):
		return _StoreFileArray(self.path)



def _StoreFileArray(path):
    # file_name = abspath(raw_input("Enter file name:"))
    # self=abspath(raw_input("Enter file name:"))
    try:
        nums=open(path).read().split()
        
        for i in range(len(nums)):
            nums[i]=re.sub('\W',"",nums[i].lower())
            nums[i]=re.sub('\d',"",nums[i]) #I didn't realize this doesn't capture "_" for some reason
            #I didn't realize that this loop does not remove empty elements
        

    except IOError:
        print path, "can't be opened." #This did not work right"
    else:
        return nums

