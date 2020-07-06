import requests as req
from bs4 import BeautifulSoup as bs4
import os


HOST = 'https://tengrinews.kz'
URL = 'https://tengrinews.kz/tag/%D0%9A%D0%BE%D1%80%D0%BE%D0%BD%D0%B0%D0%B2%D0%B8%D1%80%D1%83%D1%81/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
FILE = 'number.txt'

def base (URL):
    r = req.get(URL, headers=HEADERS)
    return r
def napoln(code):
    soup = bs4(code.text, 'html.parser')
    kol = soup.find('div', class_='tn-news-author-list-item')
    a = {
        'title' : kol.find('span', class_='tn-news-author-list-title').get_text(),
        'img' : kol.find('div', class_='tn-image-container').find('img').get('src'),
        'content' : kol.find('p', class_='tn-announce').get_text()+'...',
        'link' : kol.find('a', class_='tn-link').get('href')
    }
    a1  = a['link']
    k=lastnumber(a1)
    return a,k
    

    
def lastnumber(num):
    k = ''
    with open(FILE, 'r', encoding = 'utf-8') as g:
        if (g.read()!=num):
            k = 'no'
        g.close()
    with open(FILE, 'w', encoding = 'utf-8') as g:
        g.write(num)
        g.close()
    return k

def parsing ():
    code = base(URL)
    if code.status_code==200:
        a,s=napoln(code)
        return a,s
