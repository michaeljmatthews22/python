__author__ = 'jegber17'

#Import modules

import glob
import re
import tkinter
from tkinter.messagebox import showinfo
from tkinter.filedialog import askdirectory

#Open outfile

#Establish a class for the two major function

class input:

    #Create a function that asks for directory and add .txt ending

    def read_files():
        directory = askdirectory()
        input.path = directory + '/*.txt'

    #Create a function that counts the feature and print to outfile

    def counts(feature):
        file_out = open('counts_GUI.csv', 'w+')         #open a CSV outfile
        file_out.write('Filename' + ',' + entry.get() + '\n')

        for file in glob.glob(input.path):
            word_count = 0
            count = 0
            with open(file, encoding='utf-8', errors='ignore') as file_in:
                text = file_in.readlines()
                for line in text:
                    if not re.match("^<", line):
                        words = line.split()

                        for word in words:
                            word_count += 1
                            word = word.lower()
                            if word == entry.get():
                                count +=1

            word_normed = count/word_count*1000
            file_out.write(file + ',' + str(word_normed) + "\n")


#Establish a window called 'Feature Counter' and establish the size

window = tkinter.Tk()
window.title('Feature Counter')
window.geometry('400x250')

mycolor1 = '#fb6547'
mycolor2 = '#a8f2c3'
window.configure(bg=mycolor1)

#Create a label for text selection and a button for search term input

tkinter.Label(window, text="Step 1: Select one or more texts:", bg=mycolor1, font="-weight bold").pack()
file = tkinter.Button(window, text='Browse', bg=mycolor2, command=input.read_files, font="-weight bold", borderwidth=6).pack()

#Create a label for word entry

tkinter.Label(window, text="Step 2: Enter a word:", bg=mycolor1, font="-weight bold").pack(pady=(20,0))

#Create a text entry box and store the input

entry = tkinter.Entry(window)
entry.pack()

#Define a function that contains two functions (access the search term and close the program)

def search_and_quit():
    input.counts(entry.get())
    window.destroy()

#Create a button that completes the two functions created above

button = tkinter.Button(window, text='Search', bg=mycolor2, command=search_and_quit, font="-weight bold", borderwidth=6).pack(pady=5)

#Run the application

window.mainloop()
