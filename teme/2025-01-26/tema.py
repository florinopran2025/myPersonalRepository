import os

# Task 1 ------------------------------------------------ (done)
# You have two text files. Find out if their lines match. 
# If they don't, print the mismatched line from each file.
# -------------------------------------------------------

# file1=open("C:\\_FILES\\Programare\\Python\\Curs\\teme\\2025-01-26\\task1-file1.txt","r")
# file2=open("C:\\_FILES\\Programare\\Python\\Curs\\teme\\2025-01-26\\task1-file2.txt","r")
# file1Lines=[]
# file2Lines=[]
# for line in file1:
#     file1Lines.append(line)

# for line in file2:
#     file2Lines.append(line)

# perfectMatch=0
# for i in range(0,len(file1Lines)):
#     if file1Lines[i]!=file2Lines[i]:
#         perfectMatch+=1

#         print(f"Mismatch found:\n{file1Lines[i]}(from File 1)\n{file2Lines[i]}(from File 2)")
# if perfectMatch==0:
#     print("Perfect Match. The two files are identical (Line by Line).")
# else: 
#     print("There are", perfectMatch, "different lines between the two files.")

# file1.close()
# file2.close()



# Task 2 ------------------------------------------------ (done)
# You have a text file. Create a new file and write the following 
# statistics based on the source file to it:
# Number of characters;
# Number of lines;
# Number of vowels;
# Number of consonants;
# Number of digits.
# -------------------------------------------------------

# def verifyChar(char):    
#     if 48<=ord(char) and ord(char)<=57:
#         #digit
#         return "digit"
#     if ord(char) in range (65,90) or ord(char) in range (97,122):
#         #either vowel or consonant
#         if char in ["a","e","i","o","u","A","E","I","O","U"]:
#             return "vowel"
#         return "consonant"
#     return "nothing"

# file1=open("C:\\_FILES\\Programare\\Python\\GitRepositories\\myPersonalRepository\\teme\\2025-01-26\\task1-file1.txt","r")
# chars=0
# lines=0
# vowels=0
# consonants=0
# digits=0
# for eachline in file1:
#     chars+=len(eachline)
#     lines+=1
#     for i in range (0,len(eachline)):
#         char=eachline[i]
#         print(char)
#         if verifyChar(char)=="digit":
#             digits+=1
#         if verifyChar(char)=="consonant":
#             consonants+=1
#         if verifyChar(char)=="vowel":
#             vowels+=1
# file1.close()
# writeChars="Number of chars:"+str(chars)
# writeLines="Number of lines:"+str(lines)
# writeVowels="Number of vowels:"+str(vowels)
# writeConsonants="Number of consonants:"+str(consonants)
# writeDigits="Number of digits:"+str(digits)
# #write results in task2-file1.txt
# file2=open("C:\\_FILES\\Programare\\Python\\GitRepositories\\myPersonalRepository\\teme\\2025-01-26\\task2-file1.txt","w")
# file2.write(writeChars+"\n")
# file2.write(writeLines+"\n")
# file2.write(writeVowels+"\n")
# file2.write(writeConsonants+"\n")
# file2.write(writeDigits)
# print("Results were succesfully written in the file")
# file2.close()

# Task 3 ------------------------------------------------ (done)
# You have a text file. Delete the last line from it. Write the result to another file.
# -------------------------------------------------------

# file1=open("C:\\_FILES\\Programare\\Python\\Curs\\teme\\2025-01-26\\task3-file1.txt","r")
# file1List=[]
# for line in file1:
#     file1List.append(line)
# file1.close()

# file2=open("C:\\_FILES\\Programare\\Python\\Curs\\teme\\2025-01-26\\task3-file2.txt","w")
# for i in range (0,len(file1List)-1):
#     file2.write(file1List[i])
# file2.close()

# Task 4 ------------------------------------------------- (done)
# You have a text file. Find the length of the longest line.
# --------------------------------------------------------
# file1=open("C:\\_FILES\\Programare\\Python\\GitRepositories\\myPersonalRepository\\teme\\2025-01-26\\task1-file1.txt")
# maxLength=0
# for eachline in file1:
#     if len(eachline)>maxLength:
#         maxLength=len(eachline)
# print(maxLength)
# file1.close()



# Task 5 ------------------------------------------------ (done)
# You have a text file. Count how many times the word specified by the user occurs in it.
# -------------------------------------------------------
# found=0
# def checkLine(start,line,checkWord):
#     global found
#     segment=line[start:len(line)-1] # change the segment in which the word will be checked
#     foundOn=segment.find(checkWord)
#     if foundOn!=-1: # found it
#         found+=1 # add it
#         if foundOn+len(checkWord)*2<=len(line): # is it possible to go further?
#             checkLine(foundOn+len(checkWord),line,checkWord) # go further on line

# checkWord=input("Word to check:")

# file1=open("C:\\_FILES\\Programare\\Python\Curs\\teme\\2025-01-26\\task5-file1.txt","r")
# #open file
# for line in file1:
#     checkLine(0,line,checkWord)
# print("Number of appearences:",found)
# #close file
# file1.close()


# Task 6 ------------------------------------------------
# You have a text file. Find and replace the specified word. 
# The user determines what to search for and to what it should be replaced.
# -------------------------------------------------------