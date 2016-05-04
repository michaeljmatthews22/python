#!/bin/bash

_author_ = "Michael J. Matthews"
_assignment_ = "Assignment 3"

"""
Task:

1. Choose two texts that are at least 500 words each. Try to pick one text that is more formal and one that is less formal.
2. Create a program that produces normalized counts (per 100 words) for the number of pronouns, contractions, and modals in both of these texts.
3. Make sure to check accuracy (precision and recall) and report.
4. Run your program on each text and interpret the results in about a paragraph.

"""

"""
Results:

I read through the text and found what I could. I may have been mistaken,
but I believe that I was able to count all of the pronouns, modals and contractions.

For more accurate results, further examination of the text would be necessary

Formal Text:

Beginning of Moby Dick

Precision:
    Pronouns: 17/21 80%
    Modals: 5/5 100% 
    Contractions: 0/0 100%
Recall:
    Pronouns: 17/17 100%
    Modals: 5/5 100%
    Contractions: 0/0 100%

Informal Text:

Notes from Lecture

Precision:
    Pronouns: 18/18 100%
    Modals: 3/3 100%
    Contractions:0/0 100%
Recall:
    Pronouns: 18/21 85%
    Modals: 3/3 100%
    Contractions: 0/0 100%

"""

import re
import string          

while True:

    prompt = input("\nInput text: ")

    input_text = prompt.split()
    
    #setting count for found
    count_pronouns = 0
    count_contractions = 0
    count_modals = 0
    
    #setting up lists for found pronouns
    pronouns_found = []
    contractions_found = []
    modals_found = []

    pronouns = ["i", "me", "you", "he", "she", "him", "her", "us" "we", "i'm", "you've", "they", "them", "they've",
                "they'd", "he'd", "she'd", "we'd", "i'd"
                "you'd"]

    modals = ["can", "will", "shall", "should", "could", "would", "can't'",
            "won't","shalln't", "shouldn't", "couldn't", "wouldn't'"]
    

    #these ones depend upond the context
    modals_context = ["have", "ought", "had", "able"]

    #setting a counter for the index we are in the list
    place = -1

    #setting a count for words in text
    count = 0
    
    for found in input_text:
        #stripping certain punctuation
        found = re.sub(r'\!|\?|\.|\"|\)|\(|\,|\:|\;', "", found)
        #putting everything to lower
        found = found.lower()

        #counting counters
        count = count + 1
        place = place + 1
        
        if found in pronouns or re.match("[a-z]*\'ll", found):
            if found != "it'll":
                count_pronouns = count_pronouns + 1
                pronouns_found.append(found)
        if found in modals:
            count_modals = count_modals + 1
            modals_found.append(found)
        if found in modals_context:
            goback = input_text[place - 1]
            goforward = input_text[place + 1]
            if found == "able" and goback == "be" and goforward == "to":
                modals_found.append(goback + " " + found + " " + goforward)
            if found == "have" or found == "had" or found == "ought":
                if goforward == "to":
                    modals_found.append(found + " " + goforward)
            
    for found in input_text:
        if re.match("^[a-z]*\'[^s]", found):
            count_contractions = count_contractions + 1
            contractions_found.append(found)

    #setting numbers of found/nominalization
    nominalize = 100
    number_pro = len(pronouns_found)
    number_mod = len(modals_found)
    number_con = len(contractions_found)

    #this part is necessary just in case the result
    #is 0 and we can't divide by 0

    if number_con == 0:
        nom_con = "No contactions found"
    else:
        nom_con = (number_con/count) * nominalize
    if number_pro == 0:
        nom_pro = "No pronouns found"
    else:
        nom_pro = (number_pro/count) * nominalize
    if number_mod == 0:
        nom_mod = "No pronouns found"
    else:
        nom_mod = (number_mod/count) * nominalize
    
    
    #printing data
    print("Pronouns found: ",pronouns_found)
    print("Pronouns nominalized: ", nom_pro)
    print("Modals found: ", modals_found)
    print("Modals nominalized: ", nom_mod)
    print("Contractions found: ",contractions_found)
    print("Contractions nominalized: ", nom_con)

   
        


  
    
    
      
      
    

 
      
      
    


  
