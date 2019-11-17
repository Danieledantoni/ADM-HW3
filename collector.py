
from bs4 import BeautifulSoup
import requests
import numpy as np
import time

for j in range(1,4):
    url = 'https://raw.githubusercontent.com/CriMenghini/ADM/master/2019/Homework_3/data/movies{}.html'.format(j)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # download all the html pages
    for i in range(1):
        link = str(soup.select('a')[i])[9:-4].partition("\"")[0]
        time.sleep(np.random.randint(1,6))
        movie = str(BeautifulSoup(requests.get(link).text, 'html.parser'))
        f = open('C:/Users/Sasha/Desktop/DS/ADM/HW3/movies{}/movie_{}.html'.format(j,i), 'w', encoding="utf-8")
        f.write(movie)
