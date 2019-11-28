# -*- coding: utf-8 -*-
"""
title: Tidy Route Summary Script
author: David Smith
created: 23/11/2019

Instructions:

1) Paste the route summary you want to fix up in between the triple quotes, as per the example below, with no spaces before the first letter or after the last character.

2) Click 'run'.

3) Respond to any prompts from the program in the terminal on the right-hand side of the screen.

The corrected route summary will then appear.
   
4) Highlight that text, copy it, then paste it back into the custom route summary in the portal.

If you have any feedback for me (e.g. 'It doesn't bloody work!'), I'd love to hear it. Please send a screenshot to david.smith@nhvr.gov.au | dvdsmith84@gmail.com

Thanks :)

PS: some keyboard shortcuts are slightly different when using the terminal on the right-hand side (the black area): 
- To copy, it's CTRL+INSERT
- To paste, it's CTRL+SHIFT+V
"""

import re
import string

#PASTE ROUTE SUMMARY BELOW
str1 = r"""Start: 28 Sky Rd, Melbourne Airport VIC 3045
Sky Rd, Melbourne Airport
South Centre Rd, [Melbourne Airport - Tullamarine]
Sharps Rd, Tullamarine
Airport Dr, Tullamarine
Western Ring Rd, [Tullamarine - Keilor Park]
Calder Fwy, [Keilor Park - Malmsbury]
Calder Hwy, [Malmsbury - Ravenswood]
Calder Alternative Hwy, [Ravenswood - Marong]
Calder Hwy, [Marong - Bridgewater on Loddon]
Bridgewater-Serpentine Rd, [Bridgewater on Loddon - Serpentine]
River St, Serpentine
Loddon Valley Hwy, [Serpentine - Kerang]
Murray Valley Hwy, [Kerang - Euston]
Sturt Hwy, [Euston - Mildura]
Cureton Ave, Mildura
Seventh St, Mildura
Seventh St E, Mildura
The Crescent, Mildura
Byrne Ct, Mildura
End: 6-7 Byrne Ct, Mildura VIC 3500"""










#CODE BELOW. DO NOT CHANGE OR DELETE
def tidy_route_summary():
    print('Tidy Route Summary')
    print('\n=====================================================\nRemember to check the final route summary for errors!\n=====================================================', '\n')

    lines = str1.split('\n')
    
    start_line = ''
    end_line= ''
    start_line += lines[0]
    end_line += lines[-1]
    lines.pop(0)
    lines.pop(-1)

    for line in range(len(lines)):
        lines[line] = lines[line].strip()

    lines2 = []

    for line in lines:
      if 'Offramp' not in line and 'Off ramp' not in line and 'Off-ramp' not in line and 'off-ramp' not in line and 'Off Ramp' not in line and 'Off-Ramp' not in line and 'off ramp' not in line and 'off road' not in line and 'Onramp' not in line and 'On ramp' not in line and 'On-ramp' not in line and 'on-ramp' not in line and 'On Ramp' not in line and 'On-Ramp' not in line and 'on ramp' not in line and 'on road' not in line:
        lines2.append(line)

    roads = []
    suburbs = []
    for line in lines2:
        roads.append(line[:line.find(',')])
        suburbs.append(line[line.find(',')+2:])
    
    for suburb in range(len(suburbs)):
        suburbs[suburb] = suburbs[suburb].strip()            

    word = re.compile(r'\b\w+\b')
    double_word = re.compile(r'\b\w+\s\w+\b')
    
    matches = re.findall(word, suburbs[0])
    matches2 = re.findall(double_word, suburbs[0])
    if suburbs[0] not in matches and suburbs[0] not in matches2:
            suburbs[0] = input('Please enter a valid first suburb (letters only): ')    
    
    #weed out unwanted non-alphanumeric characters    
    bad_chars = re.compile(r'[^a-zA-Z\d\s\[\]\-\|]')
    bad_char_matches = bad_chars.findall(string.printable)
    
    for suburb in range(len(suburbs)):
        for char in bad_char_matches:
            if char in suburbs[suburb]:
                suburbs[suburb] = suburbs[suburb].replace(char, ' ')
    
    suburbs_two = []
    #weed out missing suburb, whitespace, numbers and PA numbers
    for suburb in suburbs:
        if len(suburb)==0 or suburb.isspace() or suburb.isnumeric() or re.search(r'\w+\d+', suburb) != None:
            suburbs_two.append('empty')
        else:
            suburbs_two.append(suburb)
    
    suburbs_three = []
    
    suburbs_three.append(suburbs[0])
    
    sub_dash_sub = re.compile(r'\b\w+\s\-\s\w+\b')
    sub_dash_sub_double_word = re.compile(r'\b\w+\s\w+\s\-\s\w+\s\w+\b')
    left_sub_dash_sub_double_word = re.compile(r'\b\w+\s\w+\s\-\s\w+\b')
    right_sub_dash_sub_double_word = re.compile(r'\b\w+\s\-\s\w+\s\w+\b')
    brackets_sub_dash_sub = re.compile(r'\[\w+\s\-\s\w+\]')
    brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\w+\s\-\s\w+\s\w+\]')
    left_brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\w+\s\-\s\w+]')
    right_brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\-\s\w+\s\w+\]')
    
    #weed out invalid instances such as 'Suburb - Requesting intersection...' etc
    for suburb in suburbs_two[1:]:
        
        matches = re.findall(sub_dash_sub, suburb)
        matches2 = re.findall(sub_dash_sub_double_word, suburb)
        matches3 = re.findall(brackets_sub_dash_sub, suburb)
        matches4 = re.findall(brackets_sub_dash_sub_double_word, suburb)
        matches5 = re.findall(word, suburb)
        matches6 = re.findall(double_word, suburb)
        matches7 = re.findall(left_brackets_sub_dash_sub_double_word, suburb)
        matches8 = re.findall(right_brackets_sub_dash_sub_double_word, suburb)
        matches9 = re.findall(left_sub_dash_sub_double_word, suburb)
        matches10 = re.findall(right_sub_dash_sub_double_word, suburb)
        
        if suburb in matches or suburb in matches2 or suburb in matches3 or suburb in matches4 or suburb in matches5 or suburb in matches6 or suburb in matches7 or suburb in matches8 or suburb in matches9 or suburb in matches10:
            suburbs_three.append(suburb)
        else:
            print('\''+suburb+'\''+' is not a valid suburb or suburb range.')
            suburb2 = input('Please enter something valid. If unsure, have a guess or put \'Empty\': \n')
            suburbs_three.append(suburb2)
    
    suburbs_four = []
    #remove [same_suburb - same_suburb] instances and replace with first suburb in brackets
    for suburb in suburbs_three:
        matches = re.findall(word, suburb)
        matches2 = re.findall(double_word, suburb)
        if '-' in suburb and len(matches2) > 0:
            suburbs_four.append(matches2[0])
        elif '-' in suburb and len(matches) > 0:
            suburbs_four.append(matches[0])
        else:
            suburbs_four.append(suburb)
    
    suburbs_five = []        
    #handle 'empty' instances
    for i, suburb in list(enumerate(suburbs_four)):
        if suburb == 'empty':
            suburbs_five.append(suburbs_four[i-1])
        else:
            suburbs_five.append(suburb)
    
    suburbs_six = []
    #join suburbs together with '-'    
    def contiguous(lst, lst_two):
        for i, suburb in list(enumerate(lst)):
            if i != 0:
                suburb = suburb.replace(suburb, '['+lst[i-1]+' - '+suburb+']')
                lst_two.append(suburb)
            else:
                lst_two.append(suburb)
    #print(lst_two, '\n')
                
    contiguous(suburbs_five, suburbs_six) 
    
    suburbs_seven = []
    #eliminate duplicates within brackets
    for i, suburb in list(enumerate(suburbs_six)):
        front = suburb[1:suburbs_six[i].find('-')-1]
        back = suburb[suburbs_six[i].find('-')+2:-1]
        if front == back:
            suburbs_seven.append(front)
        else:
            suburbs_seven.append(suburb)

    
    joined = zip(roads, suburbs_seven)
    print('\n'+'Here is your tidied route summary:')
    print('\n'+start_line)
    for i, j in joined:
        print(i+', '+j)
    print(end_line)

tidy_route_summary()
