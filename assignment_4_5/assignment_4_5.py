author = 'Michael Matthews'

"""
•   Select 3 linguistic features that you think will vary across register categories. 
•   Identify those features (make sure to check accuracy)
•   Calculate normed rates of occurrence (per 1,000 words)

Write a brief report that contains:
Feature:
Accuracy:
Hypothesis:
Results:

"""

import re
import glob
import statistics

location = 'Mini-CORE_new/*.txt'

file_out = open('results.csv', 'w+')
file_out.write('Register, 1st Pronouns, 2nd Pronouns, 3rd Pronouns\n')

first_person = ["i", "me", "mine", "myself", "we", "us", "ours", "ourselves", "our"]
second_person = ["you","your","yours","yourself","yourselves"]
third_person = ["he", "she", "him", "her", "his", "hers", "himself", "herself"
                "they", "them", "theirs", "themselves", "their"]

first_list = []
second_list = []
third_list = []

types = ["HI_1st", "HI_2nd", "HI_3rd","ID_1st","ID_2nd", "ID_3rd",
         "IN_1st", "IN_2nd", "IN_3rd", "IP_1st", "IP_2nd", "IP_3rd",
         "LY_1st", "LY_2nd", "LY_3rd", "NA_1st", "NA_2nd", "NA_3rd",
         "OP_1st", "OP_2nd", "OP_3rd", "SP_1st", "SP_2nd", "SP_3rd"]

type_lists = {}

for a in types:
    type_lists[a] = {}

for file in glob.glob(location):
    words_count = 0
    counter = 0
    with open(file, encoding='utf-8', errors='ignore') as file_in:
        text = file_in.readlines()
        for line in text:
            if not re.match("^<.{2,}>$", line):
                words = line.split()
                
                for word in words:

                    if not re.match("<.*>", word):
                        word = re.sub("\.|\,|\:|\!|\?|\"|\'|\;|\)|\(", "", word)
                        words_count += 1
                        word = word.lower()
                        #here is where we will decide feature 1, 2 and 3
                        if word in first_person:
                            first_list.append(word)
                        elif word in second_person:
                            second_list.append(word)
                        elif word in third_person:
                            third_list.append(word)
                            
        

    
    file_section = file.split('+')
    file_section = file_section[1]
    

    length_first = len(first_list)
    length_second = len(second_list)
    length_third = len(third_list)

    nominalize = 1000

    length_first = (length_first/words_count) * nominalize
    length_second = (length_second/words_count) * nominalize
    length_third = (length_third/words_count) * nominalize

    
    sections= ["HI", "ID", "IN", "IP", "LY", "NA", "OP", "SP"]

    #I gave up on this
    
    """
    for different in sections:
        
        if file_section == different:
            type_lists['%s_1st' % different].append(length_first)
            type_lists['%s_2nd' % different].append(length_second)
            type_lists['%s_3rd' % different].append(length_third)
    """
        
    
    file_out.write(str(file_section) + "," + str(length_first) + "," + str(length_second) + "," + str(length_third) + "\n")


#Make sure to close the file
file_out.close()
