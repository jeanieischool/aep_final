#FileImport

from os.path import abspath   
import re

class FileImport:
	def __init__(self, path):
		self.path = path
        # self.path = abspath(raw_input("Enter file name:"))

	def StoreFileArray(self):
		return _StoreFileArray(self.path)



def _StoreFileArray(path):
    
    try:
        nums=open(path).read().split()
        
        for i in range(len(nums)):
            nums[i]=re.sub('\W',"",nums[i].lower())
            nums[i]=re.sub('\d',"",nums[i]) #I didn't realize this doesn't capture "_" for some reason
            #I didn't realize that this loop does not remove empty elements
        
    except IOError:
        print "No such file" #This did not work right"
    else:
        return nums

F=FileImport()
print F.StoreFileArray()