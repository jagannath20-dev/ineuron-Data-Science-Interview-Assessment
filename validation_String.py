from collections import Counter
 
def validate_str(strr):
   
    freq = Counter(strr)
     
    valuelist = list(freq.values()) 
     
    ValueCounter = Counter(valuelist)
    if(len(ValueCounter) == 1):
        return True
    elif(len(ValueCounter) == 2 and
         min(ValueCounter.values()) == 1):
        return True
       
    return False
# Driver code
print("**************************************** Test Case 1 *****************************************************")
str1 = "abcbcdabcdcabcdcabcdcabc"
print(validate_str(str1))
print("**************************************** Test Case 2 *****************************************************")
str2 = "xyzxyzxyzdfexzsdyekauexyzgdjake"
print(validate_str(str2))
print("**************************************** Test Case 3 *****************************************************")
str3 = "abcbc"
print(validate_str(str3))
