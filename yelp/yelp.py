import json
import re

#File for the output
file_out = open('yelp_data.csv', 'w+')
file_out.write('Business_ID, STARS, Numbers, Punctuation\n')


#Read the JSON review file into Python object called 'reviews'
file = "yelp.json"                           #put file location here
reviews = []                        #will store all of the reviews

with open(file) as file_2:          #open the dataset
    for line_2 in file_2:           #for each line in the dataset
        reviews.append(json.loads(line_2))  #add the review line to the list

temp_ID = ""
for review in reviews:  #iterate through the reviews
    text = review["text"].lower()   #access the actual text of the review and make it all lowercase

    #finding the two different features
    feature_numbers = 0
    feature_punct = 0
    words = text.split()
    for word in words:
        if re.match("\d", word): #finding all digits
            feature_numbers += 1
            print("Numbers")
            print(word)
        if re.match("\S*[^\w\s]\S*", word): #find any word with punctuation included. i.e. (don't, can't, !, ?)
            feature_punct += 1
            #print("Punct")
            #print(word)

    temp_ID = review["business_id"] #print the id of the business
    file_out.write(str(temp_ID) + "," + str(review["stars"]) + "," + str(feature_numbers) + "," + str(feature_punct) + "\n") #write out the id, the number of stars, and the number of terms
    reviews = []
