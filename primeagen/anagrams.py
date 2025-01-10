#input will always be lower and alpha
#anagram
# two strings - always same length? 

#function return True False
#empty string be an anagram?  

def isAnagram(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0 and len(s2) == 0:
        return True
    
    countS1, countS2 = {}, {}

    # Use the characters directly instead of indices
    for i in s1:
        if i in countS1:
            countS1[i] += 1
        else:
            countS1[i] = 1
    for i in s2:
        if i in countS2:
            countS2[i] += 1
        else:
            countS2[i] = 1
    return countS1 == countS2
        

print(isAnagram("listen", "silent") )
print(isAnagram("hello", "world") )
print(isAnagram("", ""))
