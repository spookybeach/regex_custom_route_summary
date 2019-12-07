# -*- coding: utf-8 -*-
"""
title: Tidy Route Summary Script
author: David Smith
created: 23/11/2019

If you have any feedback for me (e.g. 'It doesn't bloody work!'), I'd love to hear it. Please send a screenshot to david.smith@nhvr.gov.au | dvdsmith84@gmail.com

Thanks :)
"""

import re
import string
import streamlit as st
from PIL import Image

logo = Image.open('nhvr.jpeg')
st.image(logo)
st.title('Tidy Route Summary')
st.write('A Handy Tool for Access Facilitators')
st.header('*Remember to check the final route summary for errors!*')
st.write(' ')
st.write(' ')
summary = st.text_area('Paste route summary that needs to be fixed below.')

def tidy():
    if len(summary) > 0:
        split = summary.split('\n')
        
        first_line = ''
        last_line = ''
        first_line += split[0]
        last_line += split[-1]
        
        lines = []
        
        for line in split[1:-1]:
            lines.append(line)
        
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
                suburbs[0] = st.text_input('Please enter a valid first suburb (letters only): ', value='', key='first')
        
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
        sub_dash_sub_triple_word = re.compile(r'\b\w+\s\w+\s\w+\s\-\s\w+\s\w+\s\w+\b')
        left_sub_dash_sub_double_word = re.compile(r'\b\w+\s\w+\s\-\s\w+\b')
        right_sub_dash_sub_double_word = re.compile(r'\b\w+\s\-\s\w+\s\w+\b')
        left_triple_right_single = re.compile(r'\b\w+\s\w+\s\w+\s\-\s\w+\b')
        left_triple_right_double = re.compile(r'\b\w+\s\w+\s\w+\s\-\s\w+\s\w+\b')
        right_triple_left_single = re.compile(r'\b\w+\s\-\s\w+\s\w+\s\w+\b')
        right_triple_left_double = re.compile(r'\b\w+\s\w+\s\-\s\w+\s\w+\s\w+\b')
        brackets_sub_dash_sub = re.compile(r'\[\w+\s\-\s\w+\]')
        brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\w+\s\-\s\w+\s\w+\]')
        brackets_sub_dash_sub_triple_word = re.compile(r'\[\w+\s\w+\s\w+\s\-\s\w+\s\w+\s\w+\]')
        left_brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\w+\s\-\s\w+]')
        right_brackets_sub_dash_sub_double_word = re.compile(r'\[\w+\s\-\s\w+\s\w+\]')
        brackets_left_triple_right_single = re.compile(r'\[\w+\s\w+\s\w+\s\-\s\w+\]')
        brackets_left_triple_right_double = re.compile(r'\[\w+\s\w+\s\w+\s\-\s\w+\s\w+\]')
        brackets_right_triple_left_single = re.compile(r'\[\w+\s\-\s\w+\s\w+\s\w+\]')
        brackets_right_triple_left_double = re.compile(r'\[\w+\s\w+\s\-\s\w+\s\w+\s\w+\]')
        
        key_marker = 0
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
            matches11 = re.findall(sub_dash_sub_triple_word, suburb)
            matches12 = re.findall(left_triple_right_single, suburb)
            matches13 = re.findall(left_triple_right_double, suburb)
            matches14 = re.findall(right_triple_left_single, suburb)
            matches15 = re.findall(right_triple_left_double, suburb)
            matches16 = re.findall(brackets_sub_dash_sub_triple_word, suburb)
            matches17 = re.findall(brackets_left_triple_right_single, suburb)
            matches18 = re.findall(brackets_left_triple_right_double, suburb)
            matches19 = re.findall(brackets_right_triple_left_single, suburb)
            matches20 = re.findall(brackets_right_triple_left_double, suburb)
            
            if suburb in matches or suburb in matches2 or suburb in matches3 or suburb in matches4 or suburb in matches5 or suburb in matches6 or suburb in matches7 or suburb in matches8 or suburb in matches9 or suburb in matches10 or suburb in matches11 or suburb in matches12 or suburb in matches13 or suburb in matches14 or suburb in matches15 or suburb in matches16 or suburb in matches17 or suburb in matches18 or suburb in matches19 or suburb in matches20:
                suburbs_three.append(suburb)
            else:
                st.write('\''+suburb+'\''+' is not a valid suburb or suburb range.')
                suburb2 = st.text_input('Please enter something valid. If unsure, have a guess or put \'Empty\': \n', value='', key=key_marker)
                suburbs_three.append(suburb2)
            key_marker += 1
        
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
        st.write(' ')
        st.write(' ')
        if len(summary) > 0:
            st.success('Here is your tidied route summary:')
            st.write(' ')
            st.write(first_line)
            for i, j in joined:
                st.write(i+', '+j)
            st.write(last_line)
    else:
        st.info('Your tidied route summary is on its way!')
        
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        
        instructions = st.button('Instructions')
        
        if instructions:
            st.write('1) Paste the route summary into the box.')
            st.write('2) Respond to any prompts.')
            st.write('3) Copy the tidied route summary, paste it back into the Portal, and get on with your life.')
        else:
            st.write('How to use this tool.')
        
        faqs = st.button('FAQs')
        
        if faqs:
            st.header('What can this tool do?')
            st.write('CAN eliminate noise from your route summary, e.g. random characters, PA numbers, on- and off-ramps, and so on.')
            st.write('CAN join contiguous suburbs.')
            st.write('CAN\'T get it exactly right every time. It is the Access Facilitator\'s responsibility to check the final route summary for errors. You may even still need to continue fixing it up a little more. Sorry.')
            st.header('Who is this program for?')
            st.write('Access Facilitators, mainly.')
        else:
            st.write('What this tool can and can\'t do.')

if __name__ == '__main__':
    tidy()