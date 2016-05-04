_author_ = "Michael Matthews"

"""
This script is designed to go through each of the links within jod.mrm.org and
webscrape and then edit the contents of each site.

All of the code comes from online sources and class. Espcially in the formatting
of the headers to send the html request

"""

#Importing libraries
import urllib.request
import re
import os
from bs4 import BeautifulSoup

current_file = open('/Users/michael/Desktop/Volume.txt','wb')
#there are 26 volumes of the JofD
for x in range(1,27):

    #base url
    url = "http://jod.mrm.org/%d/" % x

    #I found this code online. Apparently this is how you need to encode your webscrape
    #in the headers in order to get into the website
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent':user_agent,}

    #the format that the request needs to be in
    request = urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    data = response.read()

    #Regular expression given in class to find hyperlinks
    all_links = re.findall(b'<a\s*href=[\'|"](.*?)[\'"].*?>', data)

    #looping through each of the sub links
    #i.e. http://jod.mrm.org/1/1, http://jod.mrm.org/1/2, etc. (However not all the links are 1,2,3.. sometimes it goes 1,6,10, etc.)
    for subLink in all_links:

        #converting the return of bytes into string
        subLink = str(subLink)

        #removing the 'b'' within the sublink
        subLink = re.sub('b\'', "", subLink)

        #resetting the url
        url = "http://jod.mrm.org/%s" % subLink

        #requesting data once again for that specific webiste
        user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
        headers={'User-Agent':user_agent,}

        #format to get the data
        request=urllib.request.Request(url,None,headers)
        response = urllib.request.urlopen(request)
        data = response.read()

        soup = BeautifulSoup(data, 'html.parser')
        #formatting the code, found this online as well
        for script in soup(["script", "style"]):
            script.extract()

        #getting text from file
        text = soup.get_text()

        #this is going through each line and splitting it up
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))

        #getting rid of blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)


        #reformatting the subLink to replace / and '
        subLink = re.sub('\/',"-",subLink)
        subLink = re.sub('\'',"",subLink)

        #Write to folder and file of volume


        #writting with specific encoding
        current_file.write(text.encode("utf-8"))

#make sure to close the file
current_file.close()
