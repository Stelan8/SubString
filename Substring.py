class Solution():
 
 def __init__(self,substring = "",Length_of_substring = None):
 	self.substring = substring
 	self.Length_of_substring=Length_of_substring
 	
 def longsubstring(self):
    self.substring = ""
    self.Length_of_substring = 0
    
    instring = input("Enter a string: ")
    p1 = len(instring)
    print(f"The length of the string is {p1}")
    print("")
    List = instring
    setstr = set(List)
    self.Length_of_substring = len(setstr)
    Temp = list(setstr)
    
    for i in range(self.Length_of_substring):
     self.substring += Temp[i]
     
    print("The substr is:"+self.substring)
    print(f"The length of substr is {self.Length_of_substring}")
    	            	
Solution().longsubstring()
 
