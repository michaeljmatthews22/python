__author__ = 'jegber17'
import re
count = 0
file = "file.txt"

with open(file) as file_in:       #open file handle
    text = file_in.readlines()    #read each line into 'text'
    #for line in text:             #for each line in 'text'
        #print (line)              #print the contents of 'line'

with open(file) as file_in:
    text = file_in.readlines()
    for line in text:
        if not re.match("^<", line):         #if the current line does NOT begin with '<'
            words = line.split()             #split the line into words





count_the = 0
with open(file) as file_in:
    text = file_in.readlines()
    for line in text:
        if not re.match("^<", line):
            words = line.split()
            for word in words:              #for each 'word' in the current 'words' list
                #print (word)               #print 'word'
                count = count + 1
                word = word.lower()
                if re.match("^the$",word):
                    #print(word)
                    count_the = count_the + 1
print("Number of words: ")
print(count)
print("Number of 'the': ")
print(count_the)
nom = (count_the/count) * 100
print("Nominalized count: ")
print(nom)
                



#Now add to what we have so far to count the number of definite articles (the) in the text



# with open(file) as file_in:
#     text = file_in.readlines()
#     for line in text:
#         if not re.match("^<", line):
#             words = line.split()
#
#             for word in words:
#                 word = word.lower()
#                 if re.match("^the$", word): #if 'the' is found in the current 'word'
#                     count +=1               #add 1 to the count
#                     print (word,"\t\t\t****",count)            #print 'word'
#
#                 else:
#                     print(word)
#
# print (str(count))



# word_count = 0                 #establish a word count variable
#
# with open(file) as file_in:
#     text = file_in.readlines()
#     for line in text:
#         if not re.match("^<", line):
#             words = line.split()
#
#             for word in words:
#                 word_count += 1    #add 1 to the word count for each word
#                 word = word.lower()
#                 if re.match("^the$", word):
#                     count +=1
#
# print (str(count))
# print (str(word_count))         #print the total word count
# count_normed = (count/word_count*100)
# print ((count + 0.0)/word_count*100)
#
# print(round(count_normed, 2))
