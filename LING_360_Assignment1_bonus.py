#!/bin/bash
import re

_author_ = "Michael J. Matthews"
_assignment_ = "Assignment 1"
"""
Task:

Requests a noun

Converts singular nouns into plural nouns or plural nouns into singular and prints

Do the best you can to account for irregular forms and exceptions.
You won’t be able to get them all, but you should be able to get
the program to catch most forms.

Comments:

This program is designed to get the singular form of a verb and convert it.
Due to the nature of the script there isn't as much error catching so please
verify that your spelling is correct. The program will run until 'quit' is
entered.

Enjoy!

"""


#The line below is meant to be a placeholder until the user
#enters in 'quit'

keep_going = "placeholder"

while keep_going != "quit":

  printed = "false"

  #the input from the user
  noun = input("\nPlease enter a singular or plural noun: (Enter quit to leave)\n")

  noun = noun.lower()
  #gets the last two letters from the inputted word
  last_letters = noun[-2:]

  #gets ONLY the last letter
  last_character = noun[-1:]

  singular_with_s = ["class", "business", "kiss", "bus", "gas", "measles",
                     "shambles", "address", "boss", "class", "cross",
                     "dress", "glass", "lens", "plus", "prospectus",
                     "virus", "abyss", "bass", "brass", "carcass",
                     "chess", "goddess","tweezers", "walrus"]
  
  plural_with_a = ["criteria", "phenomena", "automata"]

  #list of irregular nouns that do not change when pluralized
  irregular_stay = ["fish", "sheep", "barracks", "moose", "deer", "chess", "floss", "grass"]

  #list of irregular nouns that are given different pluralized forms
  #note, that the singluar precedes the plural form of that word
  #because there could be so many exceptions, we simply had to hard code in
  #these irregulars
  
  irregular_different = ["foot", "feet", "tooth", "teeth", "goose",
                         "geese", "child", "children", "man", "men",
                         "woman","women", "person", "people", "mouse", "mice"]

  #list of irregular nouns that are foreign followed by their special plural form
  irregular_foreign = ["alga", "algae", "amoeba", "amoebae", "antenna",
                       "antennae", "formula", "formulae",
                       "larva", "larvae","nebula", "nebulae", "vertebra",
                       "vertebrae", "corpus", "corpora", "genus", "genera", "alumnus",
                       "alumni","bacillus","bacilli","cactus","cacti",
                       "focus", "foci", "fungus", "fungi", "nucleus",
                       "nuclei","octopus", "octupi", "radius", "radii",
                       "stimulus", "stimuli", "syllabus", "sllabi",
                       "terminus", "termini", "addendum", "addenda", "bacerium",
                       "bacteria", "cirriculum", "cirricula", "datum",
                       "data", "erratum", "errata", "medium", "media", "memorandum",
                       "memoranda", "ovum", "ova", "stratum", "strata",
                       "symposium", "symposia", "apex", "apices",
                       "appendix", "appendices", "cervix", "cervices",
                       "index", "indices", "matrix", "matrices",
                       "vortex", "vortices"]

  if noun in irregular_foreign:
    location = irregular_foreign.index(noun)
    if location % 2 == 0:
      kind = "singular"
    else:
      kind = "plural"
  elif noun in irregular_different:
    location = irregular_different.index(noun)
    if location % 2 == 0:
      kind = "singular"
    else:
      kind = "plural"
  elif last_character == "s":
    if last_letters == "is":
      kind = "singular"
    elif noun in singular_with_s:
      kind = "singular"
    else:
      kind = "plural"
  elif last_character == "a":
    if noun in plural_with_a:
      kind = "plural"
  else:
    kind = "singular"

  #if inputted noun is 'quit' program exits
  if noun == "quit":
    keep_going = "quit"

  #irregular_stay
  elif noun in irregular_stay:
    print(noun)
    printed = "true"

  #irregular_different
  elif noun in irregular_different:

    #finding the location of the irregular noun in the list
    location = irregular_different.index(noun)

    if location % 2 == 0:
      #pluralized form is one after, singularize is one before
      pluralize = 1
    else:
      pluralize = -1
      
    print(irregular_different[location + pluralize])
    printed = "true"

  #irregular_foreign
  elif noun in irregular_foreign:
    #finding the location of the irregular noun in the list
    location = irregular_foreign.index(noun)

    if location % 2 == 0:
      pluralize = 1
    else:
      pluralize = -1
    print(irregular_foreign[location + pluralize])
    printed = "true"

    #this elif statement MUST proceed the one after it. Due to the different
    #nature of 's' ending nouns, if it is 'is' then this rule applies


  if kind == "singular" and printed == "false":
    
    #transforming into plural
    if last_letters == "is":
      new_noun = noun[:-2] + "es"
    elif last_letters == "ch" or last_character == "x" or last_character == "s" or last_character == "z":
      new_noun = noun + "es"
    elif last_character == "y":
      #regular expression to discover nature of 'y' ending noun
      if re.match("a|e|i|o|u\y", last_letters):
        new_noun = noun + "s"
      else:
        new_noun = noun[:-1] + "ies"

    elif last_character == "o":
      #list of exceptions specifically related to 'o' ending nouns
      exceptions = ["auto", "kangaroo", "kilo", "memo", "photo", "piano", "pimento", "pro",
              "solo", "soprano", "studio", "tattoo", "video", "zoo"]
      #setting print_once to false. As it goes through, in order to avoid printing
      #duplications of the same noun, once the noun has been printed once, it will not print again
    
      print_once = "false"
      for exception_o in exceptions:
        if exception_o == noun:
          new_noun = noun + "s"
          print_once = "true"
      if print_once == "false":
        new_noun = noun + "es"

    #going through different 'f' sounding endings    
    elif last_character == "f":
      new_noun = noun[:-1] + "ves"
      
    elif last_letters == "fe":
      new_noun = noun[:-2] + "ves"
    
    elif last_letters == "on":
      new_noun = noun[:-2] + "a"
  
    #if all else fails, tack an 's' onto the end!
    else:
      new_noun = noun + "s"

  #this is if the word is plural and not irregular
  elif kind == "plural" and printed == "false":
    is_nouns = ["analyses", "axes", "bases", "crises",
                "disagnoses", "emphases", "hypotheses",
                "neuroses", "oases", "parentheses",
                "synopses", "theses"]
    if noun in is_nouns:
      new_noun = noun[:-2] + "is"
    elif re.match(".*[es | ch | x]es$", noun):
      new_noun = noun[:-2]
    elif re.match(".*ys$",noun):
      new_noun = noun[:-1]
    elif re.match(".*ies$",noun):
      new_noun = noun[:-3] + "y"
    elif re.match(".*oes$",noun):
      new_noun = noun[:-2]
    elif re.match(".*ves$",noun):
      f_ending = ["leaves", "hooves", "selves", "elves", "wolves", "calves", "halves",
                  "loaves", "shelves", "theives", "dwarves",
                  "hooves", "scarves", "stafves", "wharves"]
      if noun in f_ending:
        new_noun = noun[:-3] + "f"
      else:
        new_noun = noun[:-3] + "fe"
    elif last_character == "a":
      new_noun = noun[:-1] + "on"
    else:
      new_noun = noun[:-1]
      
  if printed == "false" and noun != "quit":
    #printing new noun
    print(new_noun)
      
      
    


  
