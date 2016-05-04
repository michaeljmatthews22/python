_author_ = "Michael Matthews"

import glob
import re
#used for encoding on the output of each file
import io

path = "Mini-CORE_new/*.txt"

#file of words that need to be removed
function_words = "file.txt"

#list of words that we need to exclude
function_list = []
all_types = []


#the following is to put all the words within file.txt
#will be put into a list that will then be sorted
with open(function_words, encoding='utf-8', errors='ignore') as the_file:
    word_functions = the_file.readlines()
    for line in word_functions:
        words = line.split()
        for x in words:
            x = x.lower()
            function_list.append(x)

#use function_list to search for words to be removed

for file in glob.glob(path):

    #getting the register name
    register = file.split('+')
    register = register[1]

    #To get all the types of texts
    if register not in all_types:
        all_types.append(register)

    words_all = []
    counts = {}

    most_recent = "HI"

    for file in glob.glob(path):
        current_register = file.split('+')
        current_register = current_register[1]

    if current_register != most_recent:
        most_recent = current_register
        words_all = []
        counts = {}



    if register == current_register:

        file_out = io.open('%s.csv' % register, "w+", encoding='utf8')

        with open(file, encoding = 'utf-8', errors='ignore') as file_in:

            text = file_in.readlines()
            for line in text:

                #removing headers
                if not re.match("^.{2,}>$", line):
                    words = line.split()

                    for word in words:
                        if not re.match("<.*>", word):
                            word = re.sub("\.|\,|\:|\!|\?|\"|\'|\;|\)|\(|\*|\^|[0-9]|\s", "", word)
                            word = word.lower()

                            if word not in function_list:
                                if re.match("\W*", word):
                                    length = len(word)
                                    if length > 1:
                                        #trying to exlude spaces, etc.
                                        words_all.append(word)

        for w in words_all:
            #put each word into a the dictionary counts along with its number of occurences
            counts[w] = counts.get(w,0) + 1

        for i in sorted(counts, key = counts.get, reverse=True):

            #output data
            file_out.write(str(i) + "," + str(counts[i]) + "\n")


    #make sure to close each file
    file_out.close()
