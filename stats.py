__author__ = 'jegber17'
import re
import glob                            #import glob module
import statistics

path = "AWE_untagd\*.txt"                   #any .txt file in this location

file_out = open('counts_the.csv', 'w+')         #open a CSV outfile
file_out.write('ID,Register,Discipline,the\n')               #write column labels to the outfile

BI_list = []
HI_list = []

for file in glob.glob(path):
    word_count = 0
    count = 0

    file_split = file.split("\\")
    name_split = file_split[1].split("_")
    ID_split = name_split[2].split(".")

    ID = ID_split[0]
    register = name_split[0]
    discipline = name_split[1]

    with open(file, encoding='utf-8', errors='ignore') as file_in:
        text = file_in.readlines()
        for line in text:
            if not re.match("^<", line):
                words = line.split()

                for word in words:
                    word_count += 1
                    word = word.lower()
                    if re.match("^the$", word):
                        count +=1

    the = count/word_count*1000                     #assign normed count to a variable 'the'
    file_out.write(ID + ',' + register + ',' + discipline + ',' + str(the) + "\n")    #print filename and normed counts to the CSV outfile

    if discipline == 'BI':
        BI_list.append(the)
    elif discipline == 'HI':
        HI_list.append(the)

print("Stat\t" + "BI\t\t" + "HI")
print("Median:" + "\t" + "%.2f" % round(statistics.median(BI_list), 2) + "\t" + "%.2f" % round(statistics.median(HI_list), 2))
print("Mean:" + "\t" + "%.2f" % round(statistics.mean(BI_list), 2) + "\t" + "%.2f" % round(statistics.mean(HI_list), 2))
print("StdDev:" + "\t" + "%.2f" % round(statistics.stdev(BI_list), 2)+ "\t" + "%.2f" % round(statistics.stdev(HI_list), 2))
