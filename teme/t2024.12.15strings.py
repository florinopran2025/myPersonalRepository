# Task 1
# The user types in a string. Check if this string is a palindrome. 
# A palindrome is a word or text that reads the same backward as forward. 
# For instance, racecar; "Do geese see God?"; tenet; "Was it a car or a cat I saw?"

# --------------------------------------------------------------------
#SOLUTION FOR TASK 1
# --------------------------------------------------------------------

# def eliminateNonLetters(wordList):
#     """Should eliminate all characters that are not letters - using ASCII codes."""
#     # ASCII codes for a..z = 97-122 / A..Z = 65-90
#     wordList=[i for i in wordList if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122)]
#     return wordList

# comp="Computer: "
# user="\nYou: "
# string=input(f"{comp}What's your text?{user}")

# stringList=eliminateNonLetters(list(string))
# duplicate=stringList

# stringLength=len(string)
# length=len(stringList)
# print(f"{comp}{string} has {stringLength} characters, from which {length} are letters.")

# for i in range (0,int(length/2)):
#     print(f"{comp}I\'m changing {duplicate[i]} (position {i}) with {duplicate[length-i-1]} (position {length-i-1})")
#     aux=duplicate[i]
#     duplicate[i]=duplicate[length-i-1]
#     duplicate[length-i-1]=duplicate[i]

# print(f"{comp}The reverse of {stringList} is {duplicate}.")
# if stringList==duplicate:
#     print(f" As you can see, your word is a palindrome.")
# else:
#     print(f" As you can see, your word is NOT a palindrome.")


# Task 2
# The user types in text followed by a list of reserved words. 
# Find all reserved words in the text and change lowercase to uppercase there. 
# Print the modified text.

# --------------------------------------------------------------------
#SOLUTION FOR TASK 2
# i changed it lower to upper and upper to lower
# --------------------------------------------------------------------

# def upperLowerCaseWord(word):
#     # ASCII codes for a..z = 97-122 / A..Z = 65-90
#     # uppercase = -32 / lowercase= +32   
#     wordList=list(word)
#     wordlist=[chr(ord(i)-32) if 97<=ord(i)<=122 else chr(ord(i)+32) if 65<=ord(i)<=90 else i for i in wordList]
#     finalWord="".join(wordlist)
#     return finalWord

# comp="Computer: "
# user="\nYou: "
# string=input(f"{comp}What's your text?{user}")
# duplicateString=string
# stringLen=len(string)

# reserved=input(f"{comp}List of reserved words, separated by comma:{user}")
# reserved=reserved.split(",")
# reservedNo=len(reserved)
# print(f"{comp}Your reserved words are: {reserved}.")

# # change each occurrence of reserved[i] in string
# for i in range (0,reservedNo):
#     reservedWord=reserved[i]
#     for index in range(stringLen):
#         if ("".join(string[index:index+len(reservedWord)])).lower()==reservedWord.lower():
#             modified=upperLowerCaseWord(string[index:index+len(reservedWord)])
#             firstPart=""
#             if index>0: # there is something to add
#                 firstPart=string[0:index]
#             lastPart=""
#             if index+len(reservedWord)<len(string): # there is something to add
#                 lastPart=string[index+len(reservedWord):]
            
#             string=firstPart + modified + lastPart
#             print(f"{comp}:found {duplicateString[index:index+len(reservedWord)]} and modified with: {modified}.")
#             # print(string)

# print(f"{comp}: Here it is: \'{string}\'")



# Task 3
# There is some text. Count the number of sentences in it and print the result.

# --------------------------------------------------------------------
#SOLUTION FOR TASK 3
# --------------------------------------------------------------------

string=input("Type a phrase: ")
punctuation=[".","!","?"]
number=0
for index in range (len(string)):
    for i in range (len(punctuation)):
        if string[index]==punctuation[i]:
            number+=1
print(f"Based on punctuation marks, you have {number} sentences.")

