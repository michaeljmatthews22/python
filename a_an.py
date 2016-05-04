import re

keep_going = "placeholder"

while keep_going != "quit":
    sentence = input("Enter sentence with emotion:\n")

    words = sentence.split()
    printed = "false"
    for word in words:
        if re.match("[: | =]-*\).*", word):
            printed = "true"
            print("You must be happy")
        elif re.match("[: | =]-*\(.*", word) and printed != "true":
            print("You must be upset")
            printed = "true"
    if printed != "true":
        print("no emotions")
        

    

    
