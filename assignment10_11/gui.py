#Import modules
import glob
import re
import tkinter
from tkinter.filedialog import askdirectory

#Establish a class for the two major function

class input:

    #Create a function that asks for directory and add .txt ending

    def read_files():
        directory = askdirectory()
        input.path = directory + '/*.txt'

    #Create a function that counts the feature and print to outfile

    def counts(feature):

        output = tkinter.Tk()
        output.title('Find Concordance Texts')
        output.geometry('450x175')

        text_window = tkinter.Text(output, width=125, height=40)
        text_window.tag_configure('tag-center', justify='center')

        scrollbar = tkinter.Scrollbar(text_window)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        text_window.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=text_window.yview)

        #establishing lists
        input.before = []
        input.keyword = []
        input.after = []

        #setting 's' to a space
        s = " "

        for file in glob.glob(input.path):

            with open(file, encoding='utf-8', errors='ignore') as file_in:
                text = file_in.readlines()
                regex_input = entry.get()
                for line in text:

                    if not re.match("^.{2,}>$", line):
                        words = line.split()

                        length = len(words)
                        for x, word in enumerate(words):
                                if re.match(regex_input, word):
                                    if x < 6:
                                        input.before.append(s.join(words[:x]))
                                        input.keyword.append(words[x])
                                        input.after.append(s.join(words[x+1:x+5]))
                                    elif x + 5 > length:
                                        input.before.append(s.join(words[x-5:x]))
                                        input.keyword.append(words[x])
                                        input.after.append(s.join(words[x+1:]))
                                    else:
                                        input.before.append(s.join(words[x-5:x]))
                                        input.keyword.append(words[x])
                                        input.after.append(s.join(words[x+1:x+6]))


        for a, b, c in zip(input.before, input.keyword, input.after):
            text_window.insert(tkinter.INSERT, a + "     " + b.upper() + "     " + c + "\n", 'tag-center')

        text_window.pack(fill=tkinter.BOTH, expand=1)
#Establish a window called 'Feature Counter' and establish the size

window = tkinter.Tk()
window.title('Directory and Search')
window.geometry('400x175')

#Create a label for text selection and a button for search term input

tkinter.Label(window, text="Step 1: Select a directory:").pack()
file = tkinter.Button(window, text='Browse', command=input.read_files).pack()

#Create a label for word entry

tkinter.Label(window, text="Step 2: Enter a word:").pack()

#Create a text entry box and store the input

entry = tkinter.Entry(window)
entry.pack()

#Define a function that contains two functions (access the search term and close the program)

def search_and_quit():
    input.counts(entry.get())
    window.destroy()

#Create a button that completes the two functions created above

button = tkinter.Button(window, text='Search', command=search_and_quit).pack()

#Run the application

window.mainloop()
