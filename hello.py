
"""
print("Hi there ,I am here to learn python after many days :)")
print("Let's do our best okkay ")
print("I really want a good job some day inshallah ")
print("That's why i am going to work very hard from now onwards")
print("Hope it is going to be good ")


age = 19
txt = 'My name is Taliya and I am {} '
print(txt.format(age))

Name = 'Sufiya'
txt1 = 'My other name is {1} and I am {0} as well'
print(txt1.format( age , Name))



#Program to find the number of consonants and vowels in the string
str = input("Enter the string")
Vowels = "AEIOUaeiou"
no_vowels=0
for i in str:
    if i in Vowels:
        no_vowels+=1
no_consonants = len(str)-no_vowels
print('The number of vowels  are:',no_vowels)
print('The number of Consonants are:', no_consonants)


#Program Written by Chatgpt

s=input('Enter the string')
def count_vow_cons(s):
    vowels = "AEIOUaeiou"
    vowel_count = sum(1 for char in s if char in vowels)
    consonant_count = len(s)-vowel_count
    return vowel_count,consonant_count
print(count_vow_cons(s)) 


#Now Write a program to find if the given String is palindrome or not 
#My program 

s = input("Enter the string:")
def is_palindrome(s):
    s = s.lower().replace(" ","")
    return s == s[::-1]
print(is_palindrome(s))

s = input("Enter the string:")
def reverse_string(s):
    return ''.join(reversed(s))
print(reverse_string(s))


#String based program to find if the given strings are anagram of each other .

Str1 = input("Enter the String1:")
str2 = input("Enter the string2:")
def str_anagram(str1 , str2 ):
    return sorted(str1)==sorted(str2)
res = str_anagram(Str1 , str2)
if res==True :
    print("The given two strings are anagram")
else:
    print("No they are not anagram")



s = input("Enter the string:")
def compress_string(s):
    compressed = " "
    count = 1
    for i in range(1, len(s)):
        if s[i]==s[i-1]:
            count +=1
        else:
            compressed +=s[i-1] + str(count)
            count = 1
    compressed +=s[i-1] + str(count)
    return compressed if len(compressed) < len(s) else s

print(compress_string(s))#codewronghavetocheck


str1 = input("Enter the string:")
str2 = input("Enter the string:")
def is_rotation(str1 , str2):
    if len(str1) != len(str2):
        return False
    return str2 in str1 +str1
print(is_rotation(str1,str2))

### email slicer
email = input("Enter your Email:").strip()
username = email[:email.index('@')]
domain = email[email.index('@')+1:]
print(f"your username is {username} & domian is {domain}")


"""


