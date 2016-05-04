__author__ = 'jegber17'

import re, urllib.request
from bs4 import BeautifulSoup
import os
while True:
    try:
        #Establish a text ID counter
        text_ID = 1

        if not os.path.exists("/Users/michael/Documents/Winter 2016/Ling_360/Web_Corpus"):
            os.makedirs("Web_Corpus")

        #Request a seed URL
        print ("Enter the URL you wish to crawl (include the 'http://'):")
        myurl = input("@> ")

        #Remove page information from the seed URL in order to store root
        root = re.sub("/\w+\.html", "", myurl)

        #Read in the HTML and find all the hyperlinks
        html = urllib.request.urlopen(myurl)
        html = html.read()
        links = re.findall(b'<a\s*href=[\'|"](.*?)[\'"].*?>', html)

        #Loop through all of the links
        for link in links:

            #Clean the links
            link = str(link)
            link = re.sub("^b'", "", link)
            link = re.sub("'$", "", link)

            #Concatenate link with root URL, if necessary
            if not re.match("^(http|www)", link):
                link = root + "/" + str(link)

            #Read in the HTML from the current link
            current_html = urllib.request.urlopen(link)
            current_html = current_html.read()

            #Scrape the HTML markup
            current_soup = BeautifulSoup(current_html, "html.parser")
            current_clean_text = current_soup.getText()

            #Write clean text to a unique file
            current_textfile = open('/Users/michael/Documents/Winter 2016/Ling_360/Web_Corpus/ ' + str(text_ID) + '.txt','wb')
            current_textfile.write(current_clean_text.encode("utf-8"))

            print("Finished processing: " + link)

            #Increment the text ID counter by 1
            text_ID += 1
            break
    except (ValueError):
            print("Try again")
