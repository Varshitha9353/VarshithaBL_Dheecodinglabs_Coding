#Palindrome check for strings

def palindromestring(str):
    result=""
    for char in str:
        result=char+result
    return result==str



str1="racecar"
str3="hello"
str4="No lemon, no melon"
str5=""
print(palindromestring(str3))
print(palindromestring(str4))
print(palindromestring(str5))