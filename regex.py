# -*- coding: utf-8 -*-

"""
title: Custom Route Summary Script
author: David Smith
created: 17/11/2019

Instructions:
    
1) Go to this website: https://repl.it/languages/python3
    
2) Copy and paste the code below (everything from line 32 onwards, inclusive) into the white space
   in the middle.
    
3) Paste the route summary you want to fix up
   in between the triple quotes, 
   as per the example below, with no spaces before
   the first road name or after the last suburb. 

4) Click 'run'.

5) The corrected route summary will appear in the terminal on the right-hand side
   of the screen.
   Highlight that text, copy it, then paste it back into the custom route
   summary in the portal.
   
If you have any feedback for me, I'd love to hear it:
david.smith@nhvr.gov.au

"""

import re

str1 = r"""Madeup Ave, [Merthyr - New Farm]
Fake St, [Teneriffe - Newstead]
Nonsense Rd, Teneriffe
Suburbless St, 
Another Suburbless St, 
Furphy Dr, [Newstead - Teneriffe]"""

pattern = re.compile(r',(\s\[?.*\]?)')

matches = pattern.finditer(str1)

suburbs = []
   
for match in matches:
    suburbs.append(match.group(1))

separated_out = []
   
for i in suburbs:
    if '-' in i:
        separated_out.append(i[:i.find('-')-1])
        separated_out.append(i[i.find('-')+2:])
    if '-' not in i and i.isspace() == False:
        separated_out.append(i)
    if i.isspace():
        separated_out.append('No suburb') 

for i in range(len(separated_out)-1): 
    if separated_out[i].startswith(' '):
        separated_out[i] = separated_out[i].strip(' ')

for i in range(len(separated_out)-1): 
    if separated_out[i] == 'No suburb':
        separated_out[i] == 'No suburb'
    if separated_out[i].endswith(']') and separated_out[i+1].startswith('['):
        separated_out[i+1] = '['+separated_out[i].strip(']')
    if separated_out[i].isalpha():
        separated_out[i] = separated_out[i-1].strip(']')
    
suburbs_corrected = []

for i in range(len(separated_out)-1):
    if separated_out[i].startswith('[') and separated_out[i+1].endswith(']'):
        suburbs_corrected.append(separated_out[i]+' - '+separated_out[i+1])
    if separated_out[i] == 'No suburb':
        suburbs_corrected.append(separated_out[i])
    if separated_out[i].isalpha():
        suburbs_corrected.append(separated_out[i])   

lines = str1.split('\n')

lines_stripped = []

for line in lines:
    lines_stripped.append(line[:line.find(',')])
    
final = zip(lines_stripped, suburbs_corrected)

for i, j in final:
    print(i+', '+j)
