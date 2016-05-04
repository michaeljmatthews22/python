#!/bin/bash
import sys
import re
import glob

regex = sys.argv[1]


f = open('Volume.txt', 'r')

before = []
keyword = []
after = []

s = " "

print('<table border="1" style="width:100%"')

for line in f:
    print('<tr>')
    words = line.split()
    length = len(words)
    for x, word in enumerate(words):
        if re.match(regex, word):
            if x < 6:
                print('<td>')
                print(s.join(words[:x]))
                print('</td>')
                print('<td>')
                keyword = words[x].upper()
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                print(keyword)
                print('</td>')
                print('<td>')
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                print(s.join(words[x+1:x+5]))
                print('</td>')

            elif x + 5 > length:
                print('<td>')
                print(s.join(words[x-5:x]))
                print('</td>')
                print('<td>')
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                keyword = (words[x]).upper()
                print(keyword)
                print('</td>')
                print('<td>')
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                print(s.join(words[x+1:]))
                print('</td>')
            else:
                print('<td>')
                print(s.join(words[x-5:x]))
                print('</td>')
                print('<td>')
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                keyword = (words[x]).upper()
                print(keyword)
                print('</td>')
                print('<td>')
                #print('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;')
                print(s.join(words[x+1:x+6]))
                print('</td>')
        print('</tr>')

print('</table')

f.close()
