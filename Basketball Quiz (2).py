#!/usr/bin/env python
# coding: utf-8

# In[101]:


import requests
from bs4 import BeautifulSoup

url = ('https://www.nbastuffer.com/2020-2021-nba-player-stats/')
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
quit = list(('q', 'quit', 'Q', 'Quit'))

player = input("What nba player would like to know about?(team)")
if player == quit:
    exit()

player1 = input("What nba player would like to know about?(position)")
if player1 == quit:
    exit()
    
player2 = input("What nba player would like to know about?(age)")
if player2 == quit:
    exit()

basketball = soup.find('table', id = 'tablepress-71')



# In[102]:


all_trs = basketball.find_all('tr')[3:]
for row in all_trs:
    tds = row.find_all('td') # array of tds
    player_name = tds[1].text
    if player_name == player:
        team_name = tds[2].text
        print(team_name)


# In[103]:


all_trs1 = basketball.find_all('tr')[1:]
for row1 in all_trs:
    tds1 = row1.find_all('td')
    player_name1 = tds1[1].text
    if player_name1 == player1: 
        team_name1 = tds1[3].text
        print(team_name1)


# In[104]:


all_trs2 = basketball.find_all('tr')[1:]
for row2 in all_trs2:
    tds2 = row2.find_all('td')
    player_name2 = tds2[1].text
    if player_name2 == player2:
        team_name2 = tds2[4].text
        print(team_name2)


# In[ ]:




