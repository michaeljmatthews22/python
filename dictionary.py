__author__ = 'jegber17'
import glob
import re



paths = ["Mini-CORE_new/*.txt", "AWE_untagd/*.txt" ]

words_all = []

first_person = ["i", "me", "mine", "we", "us", "ours", "our"]
second_person = ["you","your","yours"]
third_person = ["he", "she", "him", "her", "his", "hers",
                "they", "them", "theirs", "their"]

register_count = 0
counts_first = {}
counts_second = {}
counts_third = {}
for xu in paths:
    print(xu)
    for file in glob.glob(xu):
        line_count = 0
        register_count += 1
        with open(file, encoding='utf-8', errors='ignore') as file_in:

            text = file_in.readlines()
            for line in text:
                line_count +=1
                line = line.lower()
                line = re.sub('[^\w\s]', '', line)
                line = re.sub('\d', '', line)

    #Begin processing the file on line 6
                if line_count > 6:
                    words = line.split()

    #Append words in 'words' to 'words_all'
                    words_all.extend(words)


    #For each word 'w' in 'words_all', if the word 'w' does not exist as a key in the dictionary then add it and set its value to 0. Add 1 to the value.
    for w in words_all:
        if w in first_person:
            counts_first[w] = counts_first.get(w,0) + 1
        elif w in second_person:
            counts_second[w] = counts_second.get(w,0) + 1
        elif w in third_person:
            counts_third[w] = counts_third.get(w,0) + 1

    #Write out key-value pairs in alphabetical order
    #for i in sorted(counts):
    #    file_out.write(str(i) + "," + str(counts[i]) + "\n")

    #Write out key-value pairs by value

    nominalize = 1000

    words_count = len(words_all)

    type_list = [counts_first, counts_second, counts_third]

    first_total = 0
    second_total = 0
    third_total = 0

    final_count = []

    count = 0
    for u in type_list:
        total = 0
        count = count + 1
        for e in u:
            number = u[e]
            number = int(number)
            total = number + total


        if count == 1:
            first_total = total
            final_count.append("First Person")
            final_count.append(first_total)
        elif count == 2:
            second_total = total
            final_count.append("Second Person")
            final_count.append(second_total)
        elif count == 3:
            third_total = total
            final_count.append("Third Person")
            final_count.append(third_total)

    #print(type_list)
    counter = 0
    for xy in final_count:
        counter += 1
        if (counter & 1) != 0:
            #if it is even
            print(xy)
        else:

            nominalize = 1000
            ed = (int(xy)/words_count) * nominalize
            print(ed)
    print("\n")
