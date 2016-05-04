#!/bin/bash
import re

_author_ = "Michael J. Matthews"
_assignment_ = "Assignment 1"
"""
Task:

Requests a noun

Converts singular nouns into plural nouns and prints

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

  #the input from the user
  noun = input("\nPlease enter a singular noun: (Enter quit to leave)\n")
  
  #gets the last two letters from the inputted word
  last_letters = noun[-2:]

  #gets ONLY the last letter
  last_character = noun[-1:]

  #list of irregular nouns that do not change when pluralized
  irregular_stay = ["fish", "sheep", "barracks", "moose", "deer"]

  #list of irregular nouns that are given different pluralized forms
  #note, that the singluar precedes the plural form of that word
  #because there could be so many exceptions, we simply had to hard code in
  #these irregulars
  
  irregular_different = ["foot", "feet", "tooth", "teeth", "goose",
                         "geese", "child", "children", "man", "men",
                         "woman","women", "person", "people", "mouse", "mice"]

  #list of irregular nouns that are foreign followed by their special plural form
  irregular_foreign = ["alga", "algae", "amoeba", "amoebae or amoebas", "antenna",
                       "antennae or antennas", "formula", "formulae or formulas",
                       "larva", "larvae","nebula", "nebulae or nebulas", "vertebra",
                       "vertebrae", "corpus", "corpora", "genus", "genera", "alumnus",
                       "alumni","bacillus","bacilli","cactus","cacti or cactuses",
                       "focus", "foci", "fungus", "fungi or funguses", "nucleus",
                       "nuclei","octopus", "octupi or octopuses", "radius", "radii",
                       "stimulus", "stimuli", "syllabus", "sllabi or sllyabuses",
                       "terminus", "termini", "addendum", "addenda", "bacerium",
                       "bacteria", "cirriculum", "cirricula or cirriculums", "datum",
                       "data", "erratum", "errata", "medium", "media", "memorandum",
                       "memoranda or memorandums", "ovum", "ova", "stratum", "strata",
                       "symposium", "symposia or symposiums", "apex", "apices or apexes",
                       "appendix", "appendices or appendixes", "cervix", "cervices or cervixes",
                       "index", "indices or indexes", "matrix", "matrices or matrixes",
                       "vortex", "vortices"]

  #if inputted noun is 'quit' program exits
  if noun == "quit":
    keep_going = "quit"
    
  elif noun in irregular_stay:
    print(noun)
  elif noun in irregular_different:

    #finding the location of the irregular noun in the list
    location = irregular_different.index(noun)

    #pluralized form is one after
    pluralize = 1

    #printing the following index
    print(irregular_different[location + pluralize])

  elif noun in irregular_foreign:
    #finding the location of the irregular noun in the list
    location = irregular_foreign.index(noun) 
    pluralize = 1
    print(irregular_foreign[location + pluralize])

    #this elif statement MUST proceed the one after it. Due to the different
    #nature of 's' ending nouns, if it is 'is' then this rule applies
  elif last_letters == "is":
    new_noun = noun[:-2]
    print(new_noun + "es")

  elif last_letters == "ch" or last_character == "x" or last_character == "s" or last_character == "z":
    print(noun + "es")
  elif last_character == "y":
    #regular expression to discover nature of 'y' ending noun
    if re.match("a|e|i|o|u\y", last_letters):
      print(noun + "s")
    else:
      new_noun = noun[:-1]
      print(new_noun + "ies")

  elif last_character == "o":
    #list of exceptions specifically related to 'o' ending nouns
    exceptions = ["auto", "kangaroo", "kilo", "memo", "photo", "piano", "pimento", "pro",
            "solo", "soprano", "studio", "tattoo", "video", "zoo"]
    #setting print_once to false. As it goes through, in order to avoid printing
    #duplications of the same noun, once the noun has been printed once, it will not print again
    
    print_once = "false"
    for exception_o in exceptions:
      if exception_o == noun:
        print(noun + "s")
        print_once = "true"
    if print_once == "false":
      print(noun + "es")

  #going through different 'f' sounding endings    
  elif last_character == "f":
    new_noun = noun[:-1]
    print(new_noun + "ves")
  elif last_letters == "fe":
    new_noun = noun[:-2]
    print(new_noun + "ves")
  
  elif last_letters == "on":
    new_noun = noun[:-2]
    print(new_noun + "a")

  #if all else fails, tack an 's' onto the end!
  else:
    print(noun + "s")
    


  
