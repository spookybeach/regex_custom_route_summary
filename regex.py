# -*- coding: utf-8 -*-
"""
title: Custom Route Summary Script
author: David Smith
created: 17/11/2019

Instructions:

1) Go to this website: https://repl.it/languages/python3

2) Copy and paste the code below (everything from line 34 onwards, inclusive) into the white space
   in the middle.

3) Paste the route summary you want to fix up
   in between the triple quotes,
   as per the example below, with no spaces before
   the first road name or after the last suburb.
   Please also delete the first line containing 'Start: ' and
   the end line containing 'End: '

4) Click 'run'.

5) The corrected route summary will appear in the terminal on the right-hand side
   of the screen.
   Highlight that text, copy it, then paste it back into the custom route
   summary in the portal.

If you have any feedback for me (e.g. 'It doesn't bloody work!'), I'd love to hear it.
Please send a screenshot to david.smith@nhvr.gov.au

Thanks :)
"""

import re

str1 = r"""Test Rd, Teneriffe
Princes Mtwy Off Ramp (onto Picton Rd), Cataract
Picton Rd, [Neverwhere - ]
Unknown, ---.   
Weird St, 1234
Chars Nums and Letters, ;PA3456
Pre-approval, PA1234
Hume Mtwy, [Wilton - Berrima]
Hume Hwy, [Berrima - Marulan|wingello]
Long Hwy, [Marulan - Marulan]
Hume Hwy Off Ramp (On to Jerrara Rd), 
Marulan South Rd, Marulan
Fake St, New Farm
Made-up Ln, [Newstead - New Farm]
Cooper Cres, Marulan"""

def tidy_route_summary():
    lines = str1.split('\n')
    roads = []
    suburbs = []

    for line in lines:
        roads.append(line[:line.find(',')])
        suburbs.append(line[line.find(',')+1:])

    string_burbs = ', '.join(suburbs).strip()
    string_burbs = string_burbs.replace(' - ]', ' - NO SUBURB]')
    string_burbs = string_burbs.replace(',  ,', ', NO SUBURB,')

    pattern1 = re.compile(r'\s\W+,')
    string_burbs = pattern1.sub(' NO SUBURB,', string_burbs)

    pattern2 = re.compile(r'\s\d+,')
    string_burbs = pattern2.sub(' NO SUBURB,', string_burbs)

    pattern3 = re.compile(r'\|\w+')
    string_burbs = pattern3.sub('', string_burbs) 
    
    pattern4 = re.compile(r'[\;\-]+[\w\d]+')
    string_burbs = pattern4.sub(' NO SUBURB', string_burbs)
    
    pattern5 = re.compile(r'\w{2}\d{4}')
    string_burbs = pattern5.sub(' NO SUBURB', string_burbs)

    burbs = string_burbs.split(', ')

    suburbs = []

    for i in burbs:
        suburbs.append(i.strip())

    suburbs_corrected = []
   
    for i in suburbs:
        if '[' in i:
            dummy = []
            pattern6 = re.compile(r'(\w+)\s+\-')
            matches = pattern6.finditer(i)
            for match in matches:
                dummy.append(match.group(1))
                if i.count(dummy[0]) > 1:
                    suburbs_corrected.append(dummy[0])
                else:
                    suburbs_corrected.append(i)
        else:
            suburbs_corrected.append(i)

                
    joined = zip(roads, suburbs_corrected)

    for i, j in joined:  
        print(i+', '+j)
            
tidy_route_summary()





