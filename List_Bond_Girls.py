#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import fileinput

url = "https://en.wikipedia.org/wiki/Bond_girl"
html = urlopen(url)
soup = BeautifulSoup(html, 'html')
# soup.contents
#print(soup)
Femme_Fatale_href = soup.find('a',href="/wiki/Femme_fatale")
Bond_Girls_Table=Femme_Fatale_href.find_next('table')
Bond_Girls_Text_List=Bond_Girls_Table.text
#print(Bond_Girls_Text_List)

Actress_Count=Bond_Girls_Text_List.count("(")
Char=0
End=0
Actresses_List = []

for Actress in range(Actress_Count):
    Start = Bond_Girls_Text_List.find("(", End)
    Start += 1  # skip the bracket, move to the next character
    End = Bond_Girls_Text_List.find(")", Start)
    Result=Bond_Girls_Text_List[Start:End]
    if Actresses_List.count(Result) == 0:
        Actresses_List.append(Result)    
    
print(Actresses_List)
