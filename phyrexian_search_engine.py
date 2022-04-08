# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 00:43:42 2022

@author: Felipe
"""


# ----------- INSTALATIONS ------------
# pip install pysimplegui
# pip install pyglet

import pyglet
import PySimpleGUI as sg

# LETTER GROUPS

vowels = ["O", "J", "H", "Q", "E", "F", "G", "K", "L"]
diacritics = ["e", "w", "v", "r", "d", "q", "x", "y", "-", "+"]
separators = [" ", "|", ":", ".\\"]

#FOR FONT

rising = ["Z", "Zd", "Zq", "Zx", "Zy", "Ze", "Zw", "Zv"]
falling = ["N", "Nd", "Nq", "Nx", "Ny", "Ne", "Nw", "Nv"]
arrows = ["Ar", "Ax", "V", "Vd", "Ve", "Dd", "Cd", "Cr"]
middle_s = ["T", "Td", "Te", "Tq", "_d", "Md", "Mx", "Mw", "Mv"]
vow = ["O", "F", "G", "E", "K", "L", "Q", "H", "J"]
weird = ["-N", "-Nx", "+Nx", "-Z", "-Zx", "-Zy", "-Zw", "-Zv", "+Zx", "+Zy", "+Zw", "+Zv"]
punctuation = ["\\", "|", ":", '"', " ", "."]

all_symbols = rising+falling+arrows+middle_s+vow+weird+punctuation

# FONTS

fonts = {
        "Phyrexian Compleat":['PhyrexianCompleat.ttf', 'Phyrexian Compleat', 'phyrexian_compleat.tsv', 1],
        "Progress Engine":['ProgressEngine.otf', 'ProgressEngine', 'progress_engine.tsv', 1],
        "Phyrexian Engraved":['Phyrexian_Engraved.otf', "Phyrexian Engraved", "phyrexian_engraved.tsv", 4],
        "Horizontal Gibberish":['Phi_horizontal_gbrsh_9.8.ttf', 'Phi_horizontal_gbrsh_9.8', 'horizontal_gibberish.tsv', 1]
        }

# FUNCTIONS (word handlers)

def translit_to_font(letters:list, conversion_sheet:dict):
    result = ''
    for char in letters:
        if char in conversion_sheet.keys():
            result = result + conversion_sheet[char]
        else:
            result = result + char
    return result

def font_to_translit(letters, conversion_sheet):
    result = ''
    val_list = list(conversion_sheet.values())
    key_list = list(conversion_sheet.keys())
    for char in letters:
        if char in conversion_sheet.values():
            result = result + key_list[val_list.index(char)]
    return result

def parse_translit(raw:str):
    parsed = [char for char in raw]
    char_i = 0
    while char_i < len(parsed):
        if parsed[char_i] in ["-", "+"]:
            parsed[char_i] = parsed[char_i] + parsed[char_i+1]
            del parsed[char_i+1]
            char_i -= 1
        if parsed[char_i] in ["e", "w", "v", "r", "d", "q", "x", "y"]:
            parsed[char_i-1] = parsed[char_i-1] + parsed[char_i]
            del parsed[char_i]
            char_i -= 1
        char_i += 1
    return parsed

def remove_elements(word: str, elements:list):
    for element in elements:
        word = word.replace(element, "")
    return word

def compare_words(w1: str, w2: str, no_vow: bool = False, no_diac: bool = False):
    if no_vow:
        w1 = remove_elements(w1, vowels)
        w2 = remove_elements(w2, vowels)
    if no_diac:
        w1 = remove_elements(w1, diacritics)
        w2 = remove_elements(w2, diacritics)
    if w2.find(w1) != -1:
        return True
    else:
        return False

# SEARCH FUNCTIONS   
        
def phrx_search(query:str, no_vowel:bool, no_diacritic:bool):
    known_results = []
    raw_results = {}
    if no_vowel:
        query = remove_elements(query, vowels)
    if no_diacritic:
        query = remove_elements(query, diacritics)
        
    for word_i in range(len(transl)):
        word = transl[word_i]
        if compare_words(query, word, no_vowel, no_diacritic):
            known_results.append([eng[word_i], where[word_i], transl[word_i]])
    
    for tex_i in range(len(text_raw)):
        for word in text_raw[tex_i]:
            if compare_words(query, word, no_vowel, no_diacritic):
                if where_raw[tex_i] in raw_results.keys():
                    raw_results[where_raw[tex_i]].append(word)
                else:
                    raw_results[where_raw[tex_i]] = [word]
    return [known_results, raw_results]

def eng_search(query:str):
    results = []
    for word_i in range(len(eng)):
        lowerc = eng[word_i].lower()
        if query == lowerc:
            results.append([where[word_i], transl[word_i]])
    return results
    

# PREPARE SEARCH

# known words        
eng = []
where = []
transl = []
file = open("phrx_words.tsv", "r")
for line in file.readlines():
    line = line.rstrip("\n").split(sep="\t")
    eng.append(line[0])
    where.append(line[1])
    transl.append(line[2])
file.close()

# raw text
where_raw = []
text_raw = []
file = open("phrx_raw.tsv", "r")
for line in file.readlines():
    line = line.rstrip("\n").split(sep="\t")
    where_raw.append(line[0])
    for sep in separators:
        line[1] = line[1].replace(sep, "|")
    line[1] = line[1].replace("\\", "")
    line[1] = line[1].replace(".", "")
    text_raw.append(line[1].split("|"))
file.close()    

#ADD FONT TO PYGLET

fonts_all = ["Horizontal Gibberish",
             "Phyrexian Compleat",
             "Phyrexian Engraved",
             "Progress Engine"]
for font in fonts_all:
    pyglet.font.add_file(fonts[font][0])
    
font_size = 25


font_choice = fonts_all[1]
font_phyr = (fonts[font_choice][1], font_size)

# GET THE TRANSLITERATION TO FONT CONVERSION

font_conv = {}
def new_conv_table():
    conv_file = open(fonts[font_choice][2], "r", encoding='utf-8')
    for line in conv_file.readlines():
        line = line.rstrip("\n").split("\t")
        font_conv[line[0]] = line[1]
    conv_file.close()

new_conv_table()

#STYLE WINDOW

sg.theme('DarkAmber')

# WINDOW CONTENTS

layout = [
        [sg.T(key="-OUT-", font=font_phyr)],
        [sg.I(readonly=True, disabled_readonly_background_color=sg.theme_background_color(), border_width=0, key="-TRANSLIT-")],
        [sg.T("Transliteration Input"), sg.I(key="-TRANSLIT_IN-"), sg.B("Add")],        
        [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in rising],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in falling],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in arrows],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in middle_s],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in vow],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in weird],
           [sg.B(translit_to_font([c], font_conv), key=c, size=(fonts[font_choice][3], 1), font=font_phyr) for c in punctuation],
           [sg.T("Font:"), sg.InputCombo(fonts_all, default_value=font_choice, readonly=True, key="-FONT-"), sg.B("Change")],
           [sg.I(key="-ENG-"), sg.B("Search English")],
           [sg.B("Search"), sg.B("Delete"), sg.B("Clear"), sg.T(key="-MSG-")],
           [sg.Checkbox("Include Vowels", k="-INC_VOW-"), sg.Checkbox("Include Diacritics", default = True, k="-INC_DIAC-")]]

window = sg.Window('Phyrexian Search Engine, by Osmago', layout)

# WINDOW PROCESSING

word = ''
translit_word = ''
while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
        break
    if event == 'Clear':
        word = ''
        translit_word = ''
    elif event == 'Delete' and word != '': # update this to work based on the transliteration instead of the font
        if word[-1] == ' ':
            translit_word = translit_word[:-1]
            word = word[:-1]
        else:
            translit_word = translit_word[:-len(parse_translit(translit_word)[-1])]
            word = translit_to_font(parse_translit(translit_word), font_conv)
    elif event in all_symbols:
        translit_word = translit_word + event
        word = word + translit_to_font([event], font_conv)
    elif event == "Add":
        parse = parse_translit(values['-TRANSLIT_IN-'])
        for symb in parse:
            if symb in all_symbols:
                translit_word = translit_word + symb
                word = word + translit_to_font([symb], font_conv)
    elif event == "Change":
        font_choice = values["-FONT-"]
        font_phyr = (fonts[font_choice][1], font_size)
        font_conv = {}
        new_conv_table()
        word = translit_to_font(parse_translit(translit_word), font_conv)
        window["-OUT-"].update(word, font=font_phyr)
        for symb in all_symbols:
            window[symb].update(translit_to_font([symb], font_conv))
            window[symb].Widget.config(font=font_phyr)
            window[symb].set_size(size=(fonts[font_choice][3], 1))  
    elif event == "Search English":
        word_to_search = values["-ENG-"]
        search_results = eng_search(word_to_search)
        if search_results == []:
            window["-MSG-"].update("No result")
        else:
            window["-MSG-"].update('')
            results_layout=[]
            results_layout.append([sg.T('Results for query: '+word_to_search, font='Any 12 bold underline')])
            for result in search_results:
                results_layout.append([sg.T("In: "+result[0], font='Any 10 bold underline')])
                results_layout.append([sg.I(result[1], readonly=True, disabled_readonly_background_color=sg.theme_background_color(), border_width=0)])
                conversion = translit_to_font(parse_translit(result[1]), font_conv)
                results_layout.append([sg.T(conversion, font=font_phyr)])
            sg.Window('Search Results', layout=[[sg.Col(layout=results_layout, scrollable=True, size=(500, 500))]]).read(close=True) 
    elif event == "Search":
        good_to_go = True
        word_to_search = translit_word.rstrip(".").lstrip("\\")
        for punc in punctuation:
            if punc in word_to_search:
                window["-MSG-"].update('Please provide a query without punctuation')
                good_to_go = False
                break
        if (not values["-INC_VOW-"]) and remove_elements(word_to_search, vowels) == '':
            window["-MSG-"].update("No result")
            good_to_go = False
        if good_to_go:
            search_results = phrx_search(word_to_search, not values["-INC_VOW-"], not values["-INC_DIAC-"])
            if search_results == [[], {}] or translit_word == '':
                window["-MSG-"].update('No result')
            else:
                window["-MSG-"].update('')
                results_layout=[]
                results_layout.append([sg.T('Results from words with solid evidence', font='Any 12 bold underline')])
                for result in search_results[0]:
                    results_layout.append([sg.T(result[0]+", from "+result[1], font='Any 10 bold underline')])
                    results_layout.append([sg.I(result[2], readonly=True, disabled_readonly_background_color=sg.theme_background_color(), border_width=0)])
                    conversion = translit_to_font(parse_translit(result[2]), font_conv)
                    results_layout.append([sg.T(conversion, font=font_phyr)])
                results_layout.append([sg.T('Results all sources (including the ones above)', font='Any 12 bold underline')])
                for key, value in search_results[1].items():
                    results_layout.append([sg.T("From "+key, font='Any 10 bold underline')])
                    for result in value:
                        results_layout.append([sg.I(result, readonly=True, disabled_readonly_background_color=sg.theme_background_color(), border_width=0)])
                        conversion = translit_to_font(parse_translit(result), font_conv)
                        results_layout.append([sg.T(conversion, font=font_phyr)])
                    
                sg.Window('Search Results', layout=[[sg.Col(layout=results_layout, scrollable=True, size=(500, 500))]]).read(close=True) 
    
    window["-OUT-"].update(word)
    window["-TRANSLIT-"].update(translit_word)
    

window.close()