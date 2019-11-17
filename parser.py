from bs4 import BeautifulSoup
import requests
import numpy as np
import time
import re
import csv
import pandas as pd
from parser_utils import get_title, remove_quotes, split_names

for f in range(1,4):
    # open the html files with BeautifulSoup
    for j in range(1):
        movie = open('movies{}/movie_{}.html'.format(f,j), 'r', encoding = 'utf-8')
        movie = BeautifulSoup(movie, 'html.parser')
        # wiki page title
        title = str(movie.title.text)
        # link of the page
        link = movie.find('link', {'rel':'canonical'}).get('href')
        # in many cases the information needed are containde in the following div
        movie = movie.find('div', class_='mw-parser-output') 
        
    
        
        # few pages are disambiguations, if we get on of those we skip the iteraction of the for loop
        if title.find('(disambiguation)') != -1:
            continue 
            
        # get the title of the movie
        title = get_title(title)
        
        if movie is not None:
            # find_next() function gives the next element, that can be a 'p', a 'div', 'a', etc ( when not 
            # specified). The variable 'x' represents each of those elements, 
            # and we take them all if their name is 'p', and until we meet the element with name 'h2'
            
            # here we get the intro
            x = movie.p #this is the first paragraph
            if x is None:
                intro = 'NA'
            else:
                intro = ''
                while x.name != 'h2':
                    if x.name == 'p':
                        #print(x.text)
                        intro = str(intro) + str(x.text)
                    x = x.find_next()
                    
            # here we get the plot
            x = x.find_next('p')
            if x is None:
                plot = 'NA'
            else:
                plot = ''
                while x.name != 'h2':
                    if x.name == 'p':
                        #print(x.text)
                        plot = plot + str(x.text)
                    x = x.find_next()
                    
            # remove quotes symbols, [.], from the intro
            intro = remove_quotes(intro)               
            #### Now we extract the information from the Infobox ####
            # ge the infobox
            infobox = movie.find('table', class_ = 'infobox vevent') 
           
            # we check info only if the infobox has some information
            # we proceed only if infobox exists
            if infobox is not None:
                if len(infobox.find_all('th')) != 0:
                    # we initialize all the variables associated with the respective infos. If the infobox doesn't contain
                    # the information, then it just remains 'NA'.
                    director = producer = writer = starring = music = release = runtime = country = language = budget = 'NA'
                    film_name = infobox.th.text # the first 'th' element is the title'
                    i = 0
                    # the 'th' tags contain the 'key' (Directed by, Produced by, etc), and the 'td' the respective names.
                    for th in infobox.find_all('th'):
                        if i <= len(infobox.find_all('td')) - 1:
                            info = infobox.find_all('td')[i].text
                            if th.text == 'Directed by':
                                director = info
                            elif th.text == 'Produced by':
                                producer = info
                            elif th.text == 'Written by':
                                writer = info
                            elif th.text == 'Starring':
                                starring = info
                            elif th.text == 'Music by':
                                music = info
                            elif th.text == 'Release date':
                                release = info
                            elif th.text == 'Running time':
                                runtime = info
                            elif th.text == 'Country':
                                country = info
                            elif th.text == 'Language':
                                language = info
                            elif th.text == 'Budget':
                                budget = info
                            i += 1
            output_file = title + '\t' + intro + '\t'+plot+'\t'+director+'\t'+producer+'\t'+writer+'\t'+ starring
            output_file = output_file + '\t'+music+'\t'+release+'\t'+runtime+'\t'+country+'\t'+language+'\t'+budget
            output_file = output_file + '\t' + link
            # we cleare the output_file from the '\n' and quotes, in form [.].
            output_file = output_file.replace('\n', '')
            output_file = remove_quotes(output_file)
            output_file = split_names(output_file)
            with open('tsv_files{}/movie_{}.tsv'.format(f,j), "w", encoding = 'utf-8') as outputter:
                outputter.write(output_file)