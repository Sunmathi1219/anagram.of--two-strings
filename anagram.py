#write program that takes a string and returns true if it is an anagram of another string ,false otherwise

from collections import Counter

def anagrams(str1,str2):

    #check the length
    if len(str1)!=len(str2):
        return False
    
    #count character frequencies
    counter1=Counter(str1)
    counter2=Counter(str2)

    return counter1==counter2

str1="knee"
str2="neek"
print(anagrams(str1,str2))

str3="knee"
str4="nelt"
print(anagrams(str3,str4))
