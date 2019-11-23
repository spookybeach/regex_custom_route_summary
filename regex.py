# -*- coding: utf-8 -*-
import re
import string

#PASTE ROUTE SUMMARY BELOW
str1 = r"""Barclay Cres, Hastings
Marine Pde, Hastings
Frankston-Flinders Rd, [Hastings - Somerville]
Hawkins Rd, Baxter
Fultons Rd, [ - Baxter]
Golf Links Rd, [ - Frankston South]
Mornington Peninsula Fwy on ramp,
Mornington Peninsula Fwy, [Langwarrin South - Carrum Downs](Mornington Peninsula Fwy Off Ramp (to Eastlink))
Eastlink, [Carrum Downs - Noble Park]
Eastlink Off-Ramp (Princes Hwy), Noble Park
Princes Hwy, [Noble Park - Springvale]
Centre Rd, [Springvale - ]
Westall Rd, [Clayton South - Clayton]
Centre Rd, Springvale
Police Rd, Springvale
Princes Hwy, [Springvale - ]
Eastlink, [Noble Park - Carrum Downs]
Eastlink Off Ramp (onto Mornington Peninsula Fwy), Carrum Downs
Mornington Peninsula Fwy, [Carrum Downs - Langwarrin South]
Mornington Peninsula Fwy Off Ramp, Langwarrin South
Mornington Peninsula off ramp,
Golf Links Rd, [Langwarrin South - ]
Fultons Rd, [Baxter - ]
Hawkins Rd, Baxter
Frankston-Flinders Rd, [Somerville - Hastings]
Marine Pde, Hastings
Barclay Cres, Hastings"""

def tidy_route_summary():
    print('Remember to check the final route summary for errors! The program doesn\'t always know the best choice to make and sometimes gets it wrong :)', '\n')
    lines = str1.split('\n')
    
    for line in range(len(lines)):
        lines[line] = lines[line].strip()

    roads = []
    suburbs = []
    for line in lines:
        roads.append(line[:line.find(',')])
        suburbs.append(line[line.find(',')+2:])
    
    for suburb in range(len(suburbs)):
        suburbs[suburb] = suburbs[suburb].strip()            
    
    dummy = []
    
    word = re.compile(r'\b\w+\b')
    double_word = re.compile(r'\b\w+\s\w+\b')
    
    matches = re.findall(word, suburbs[0])
    matches2 = re.findall(double_word, suburbs[0])
    if suburbs[0] not in matches and suburbs[0] not in matches2:
            suburbs[0] = input('Please enter a first valid suburb (letters only): ')    
    
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
        matches10= re.findall(right_sub_dash_sub_double_word, suburb)
        
        if suburb in matches or suburb in matches2 or suburb in matches3 or suburb in matches4 or suburb in matches5 or suburb in matches6 or suburb in matches7 or suburb in matches8 or suburb in matches9 or suburb in matches10:
            suburbs_three.append(suburb)
        else:
            print('\''+suburb+'\''+' is not a valid suburb or suburb range.')
            suburb2 = input('Please enter something valid. ')
            suburbs_three.append(suburb2)
    
    suburbs_four = []
    #remove [suburb - suburb] instances and replace with first suburb in brackets
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
            suburbs_five.append(suburbs_four[i+1])
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
                
#        print(lst_two, '\n')
                
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
    print('\n'+'Start: ')
    for i, j in joined:
        print(i+', '+j)
    print('End: ')

tidy_route_summary()
