#FileImport

from os.path import abspath   
import re
import string


class FileImport:
	def __init__(self, path):
		self.path = path
        # self.path = abspath(raw_input("Enter file name:"))

	def StoreFileArray(self):
		return _StoreFileArray(self.path)



def _StoreFileArray(path):
    
    try:
        nums=open(path).read().split()
        uni2ascii = {ord('\xe2\x80\x99'.decode('utf-8')): ord("'")}    
        nums=[word.decode('utf-8').translate(uni2ascii).encode('ascii') for word in nums]
        #for line in nums:
        nums=[word.strip(string.punctuation) for word in nums] #.split(" ")]
            
        for i in range(len(nums)):
            nums[i]=nums[i].lower()
        nums=filter(None, nums)
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