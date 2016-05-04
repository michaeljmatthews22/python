__author__ = 'jegber17'


import re
import glob

path = "AWE_untagd/*.txt"
tagged_all = []


for file in glob.glob(path):
    line_count = 0
    with open(file) as file_in:

        name = re.split(r"\\", file)

        text = file_in.readlines()
        for line in text:
            if not re.match("^<", line):

                words = line.split()
                tagged = nltk.pos_tag(words)
                tagged_all.extend(tagged)

 
    for word in tagged_all:
        print(word)
