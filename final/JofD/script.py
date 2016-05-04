#!/bin/bash

#importing necessary libarries
import sys #imported to be able to take arguments from the php code
import re #imported to run a regular expression

regex = sys.argv[1] #the regular expression given by the end user

f = open('Volume.txt', 'r') #opening up the file with all of the JofD

s = " " #setting s to string in order to do join later on

#text is a string that will be added to. At the end, this string is printed out to the php main index.php page
#in order to speed up the processing of the file

text = '<table border="1" style="width:100%">' #establishing 'text' with beginning html code for a table

#running through each line within the file that was opened up above
for line in f:
    text += '<tr>' #adding the beginning of a row for table
    words = line.split() #splitting the line into words
    length = len(words) #finding the length of the all the words so that I can know when we are at the end or beginning of line. This is to prevent calling an item outside of range
    for x, word in enumerate(words): #going through each word within line
        if re.match(regex, word): #maching regular expression agaisnt each word
            if x < 6: #if we are at the beginning of a line, or if it is a short line
                text += '<td>' #adding beginning of column
                text += s.join(words[:x]) #adding the words that come before keyword
                text += '</td>' #ending column
                text += '<td>' #starting new column
                keyword = words[x].upper() #making the keyword Uppercase
                #text += '&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                text += keyword #adding keyword
                text += '</td>' #ending column
                text += '<td>' #starting new column
                text += s.join(words[x+1:x+5]) #adding words that come after keyword
                text += '</td>' #ending column

            elif x + 5 > length: #if the word is at the end of a sentence
                text += '<td>' #adding beginning of column
                text += s.join(words[x-5:x]) #adding the words that come before keyword
                text += '</td>' #ending column
                text += '<td>' #adding beginning of column
                keyword = (words[x]).upper() #making the keyword Uppercase
                text += keyword  #adding keyword
                text += '</td>' #ending column
                text += '<td>' #adding beginning of column
                text += s.join(words[x+1:]) #adding words that come after keyword
                text += '</td>' #ending column

            else:
                text += '<td>' #adding beginning of column
                text += s.join(words[x-5:x]) #adding the words that come before keyword
                text += '</td>' #ending column
                text += '<td>' #adding beginning of column
                keyword = (words[x]).upper() #making the keyword Uppercase
                text += keyword  #adding keyword
                text += '</td>' #adding beginning of column
                text += '<td>' #ending column
                text += s.join(words[x+1:x+6]) #adding words that come after keyword
                text += '</td>' #ending column
        text += '</tr>' #ending row

text += '</table>' #ending table

print(text) #printing out the combined results

f.close() #closing the file that was opened at the beginning
