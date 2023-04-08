'''
Reference: https://github.com/dipes08/Extracting-data-from-Google-Scholar/blob/main/Github_Google_Scholar_Scrapper.ipynb
'''

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
from time import sleep
import re
headers={'User-Agent': 'email@gmail.com'}


def get_citations(content):
    out = 0
    for char in range(0,len(content)):
        if content[char:char+9] == 'Cited by ':
            init = char+9                          
            for end in range(init+1,init+6):
                if content[end] == '<':
                    break
            out = content[init:end]
    return int(out)


def get_year(content):
    for char in range(0,len(content)):
        if content[char] == '-':
            out = content[char-5:char-1]
    if not out.isdigit():
        out = 0
    return int(out)


def get_author(content):
    for char in range(0,len(content)):
        if content[char] == '-':
            out = content[2:char-1]
            break
    return out


def get_journal(content):
  out=re.findall("-(.*)-", content)[0]
  return out


def result(keyword, source, publisher, start_year, end_year, number_of_results):

  # Start new session
  session = requests.Session()

  # Variables
  links = list()
  title = list()
  citations = list()
  year = list()
  rank = list()
  author = list()
  journal=list()
  jour=list()
  rank.append(0) # initialization necessary for incremental purposes


  # Get content 
  for n in range(0, number_of_results, 10): 
      sleep(randint(1,5))   
      url = f'https://scholar.google.com/scholar?start={n}&q={keyword}+source:%22{source}%22+%26+source:%22{publisher}%22&hl=en&as_sdt=0,11&as_ylo={start_year}&as_yhi={end_year}&as_vis=1'
      page = session.get(url, headers={'User-Agent': 'email@gmail.com'} )
      c = page.content
      
      # Create parser
      soup = BeautifulSoup(c, 'html.parser')
      
      # Get stuff
      mydivs = soup.findAll("div", { "class" : "gs_r gs_or gs_scl" })

      
      for div in mydivs:
        try:
            links.append(div.find('h3').find('a').get('href'))
        except: # catch *all* exceptions
            links.append('Look manually at: https://scholar.google.com/scholar?start='+str(n)+'&q'+keyword.replace(' ','+'))
        
        try:
            title.append(div.find('h3').find('a').text)
        except: 
            title.append('Could not catch title')

            
            
        try:
            year.append(get_year(div.find('div',{'class' : 'gs_a'}).text))
        except: 
            year.append('Could not catch title')      


        try:
            citations.append(get_citations(str(div.format_string)))
        except: 
            citations.append('Could not catch title')            
        
        try:
            author.append(get_author(div.find('div',{'class' : 'gs_a'}).text))
        except: 
            author.append('Could not catch title')   

        try:
            jour.append(get_journal(div.find('div',{'class' : 'gs_a'}).text))
        except: 
            jour.append('Could not catch title')  

        journal.append(source)
      
        rank.append(rank[-1]+1)
      
      if len(mydivs) == 0:
        break    # break here



  # Create a dataset and sort by the number of citations
  data = pd.DataFrame(zip(author, title, citations, links, year, journal, jour), index = rank[1:], 
                      columns=['Author', 'Title', 'Citations',  'Link', 'Year', 'Journal', 'jour'])

  return data


if __name__ == '__main__':
    keyword = "Deep Learning"
    source = ""
    publisher = ""  # the double quote will look for the exact keyword, # the simple quote will also look for similar keywords
    number_of_results = 100 #This number restricts the number of results. 1000 is max for google scholar
    start_year=2021
    end_year=2022


    data=result(keyword, source, publisher, start_year, end_year, number_of_results)


    data.sort_values(by='Citations', ascending=False, inplace=True)
    data.reset_index(drop=True, inplace=True)
    print(data.to_string())