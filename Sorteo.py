from bs4 import BeautifulSoup
import requests
import random
import pandas as ps

def extract_info():
    id = '6806391889948986630'
    #id=input("Introdueix el id : ")

    url = 'https://vidlan.com/video/' + id
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")

    # Filtrar info
    cm = soup.find_all('div', {'class': "srrtab2"})

    return cm

def html_save(file, cm):
    html = open(file, "a")

    for i in cm:
        html.write(str(i))

    html.close()

def info(file):
    f = open('output.txt', 'w+')
    with open(file, 'r') as read:
        for i in read.readlines():
            if "<span>" in i:
                 u = i.replace('<span>', '').replace('</span>', '').replace('\n', ' ').split('-')
                 f.write("User : @" + str(u[0]))
            elif "<p>" in i:
                p = i.replace('<p>', '').replace('</p>', '')
                f.write("|| Comment : " + str(p))

def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line('output.txt'))

file='users.txt'

html_save(file,extract_info())
info(file)

