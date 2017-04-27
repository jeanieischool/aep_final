#FileImport

from os.path import abspath   
import re
import string
import nltk

class FileImport:
	def __init__(self, path):
		self.path = path
        # self.path = abspath(raw_input("Enter file name:"))

	def StoreFileArray(self):
		return _StoreFileArray(self.path)



def _StoreFileArray(path):
    
    try:
        nums=open(path).read().split()
        nums=[word.strip(string.punctuation) for word in nums.split(" ")]
        
        # for i in range(len(nums)):
        #     nums[i]=re.sub('\W',"",nums[i].lower())
        #     nums[i]=re.sub('\d',"",nums[i]) #I didn't realize this doesn't capture "_" for some reason

        
    except IOError:
        # print "No such file" #This did not work right"
        return "No such file"
    else:
        return nums

# F=FileImport()
# print F.StoreFileArray()