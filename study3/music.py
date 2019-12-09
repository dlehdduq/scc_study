import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

target_url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20190908'
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url,headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

music_list = soup.select('.music-list-wrap > table > tbody > tr')
rank=1;

for i in music_list:
    info = i.select('td.info')
    artist = i.select_one('a.artist')
    title = i.select_one('a.title')
    
    print(rank,artist.text,(title.text).strip())

    doc = {
        'rank': rank,
        'artist': artist.text,
        'title': (title.text).strip()
    }

    db.music.insert_one(doc)
    rank+=1

#def insert_db(music):
#    db.music.insert_one(music)