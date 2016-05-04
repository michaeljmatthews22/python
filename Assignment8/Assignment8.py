_author_ = "Michael Matthews"

import glob
import re
import nltk
#used for encoding on the output of each file
import io

path = "AWE_untagd/*.txt"


#list of words that we need to exclude
function_list = []

words_all = []
counts = {}

counter = 0

for file in glob.glob(path):

    counter = counter + 1
    tagged_all = []

    current_register = re.sub('\/','\_',file)
    current_register = current_register.split('_')
    current_register = str(current_register[2]) + "_" + str(current_register[3])

    file_out = io.open('%s.csv' % current_register, "w+", encoding='utf8')

    with open(file, encoding = 'utf-8', errors='ignore') as file_in:

        text = file_in.readlines()
        for line in text:

            previous = "NOT"
            if not re.match("^.{2,}>$", line):
                tokens = nltk.word_tokenize(line)
                tagged = nltk.pos_tag(tokens)

                for x,pos in tagged:
                    if previous == "NN" or previous == "NNS":
                        if pos == "NN" or pos == "NNS":
                            com = str(previous_word) + "+" + str(x)
                            words_all.append(com)


                    if pos == "NN" or pos == "NNS":
                        previous = pos
                        previous_word = x
                    else:
                        previous = "not"

    for w in words_all:
        #put each word into a the dictionary counts along with its number of occurences
        counts[w] = counts.get(w,0) + 1


    if counter == 25:

        for i in sorted(counts, key = counts.get, reverse=True):
            joined = i.split('+')

            length_word = len(joined[0])
            length_word2 = len(joined[1])

            if length_word > 1 and length_word2 > 1:

                file_out.write(str(joined[0]) + "," + str(joined[1]) + "," + str(counts[i]) + "\n")

        file_out.close()
        counter = 0
        words_all = []
        counts = {}
