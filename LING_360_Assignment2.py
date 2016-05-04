#!/bin/bash

_author_ = "Michael J. Matthews"
_assignment_ = "Assignment 2"

"""
Task:

-Use regular expressions and lists to correctly identify and count all
of the nominalizations in a short text. You can simply paste a short
text into PyCharm for your input.

-Check the accuracy (precision and recall) of your program.
Report the initial accuracy rates, make at least one round of
improvements, and report your final accuracy rates.
"""

"""
Text used in testing

import this

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

"""
Reporting intial precision and recall

Round 1:
Precision: 4/15 (26%)
Recall: 4/4 (100%) :)

Output:

Enter paragraph with nominalizations: (Enter quit to leave)
The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!
There were 15 occurences of nominalizations
better
better
better
better
better
better
never
temptation
better
never.
never
better
implementation
implementation
honking
"""
#On Test one I made the mistake of thinking that "er" ending words were
#often times nominalizations, hence the better, never. Also I decided to strip
#punctuation and add more words. Test 2 had a much higher Precision,
#but obviously a more complex text would push its limits.

"""
Test 2:
Precision: 10/10 (100%)
Recall: 10/12 (83%)

Enter paragraph with nominalizations: (Enter quit to leave)
The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! Inventors are really important when considering nominalizations. Think about all of the murders and the change in the world of governor and actors and employees. The failure of the King is the great difficulty of our day and age. 
There were 10 occurences of nominalizations
temptation
implementation
implementation
honking
considering
nominalizations
governor
actors
employees
failure
There were 2 possible occurences.
murders
change

"""


import re
import string

#The line below is meant to be a placeholder until the user
#enters in 'quit'

keep_going = "placeholder"

while keep_going != "quit":

  printed = "false"

  #the input from the user
  prompt = input("\nEnter paragraph with nominalizations: (Enter quit to leave)\n")
  if prompt == "quit":
    quit(0)
  #stripping the string of punctuation.
  #found idea on http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
  #modified to meet needs of this script
  
  for punct in string.punctuation:
    prompt = prompt.replace(punct,"")

  #lowercasing everything
  prompt = prompt.lower()

  #splitting each word up
  prompt = prompt.split()

  #creating a list to add all nominalizations found
  all_found = []
  double_check = []

  #setting count for found
  count = 0

  #due to the fact that you would need to know the context of
  #some of the words, I but questionable ones into this possible
  #list
  count_possible = 0

  #list of words that could be a nominalization, depeding on context
  possible = ["murder","change", "murders","changes"]
  
  exceptions = ["actor","actors","inventor","inventors","sculptor","sculptors","governor",
                "governors", "translators","translator", "analysis", "failure"]
  
  for found in prompt:
    if re.match("^[ab-z]+ings?\W?$",found) or re.match("^[ab-z]+ees?\W?$",found) or re.match("^[ab-z]+ions?\W?$",found) or re.match("^[ab-z]+tances?\W?$",found) or re.match("^[ab-z]+ments?\W?$",found)  or found in exceptions:
      count = count + 1
      all_found.append(found)
    elif re.match("^[ab-z]+ors?\W?$",found) or re.match("^[ab-z]+ty\W$",found) or found in possible:
      count_possible = count_possible + 1
      double_check.append(found)

  #changing count(int) to string
  count_str = str(count)
  count_str_possible = str(count_possible)

  #printing results
  print("There were " + count_str + " occurences of nominalizations")
  for every in all_found:
    print(every)
  print("There were " + count_str_possible + " possible occurences.")
  for every_possible in double_check:
    print(every_possible)
  
    
    
      
      
    

 
      
      
    


  
