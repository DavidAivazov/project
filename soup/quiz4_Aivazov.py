import csv
import time
import random

import requests
from bs4 import BeautifulSoup

for page in range(1, 6):
    url = f'https://coreyms.com/page/{page}'
    r = requests.get(url)
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')
    video_url = soup.find('iframe', {'class': 'youtube-player'})['src']
    video_id = video_url[30:]
    print(f'video id: {video_id}')
    titles = soup.find_all('a', {'class': 'entry-title-link'})
    titles_list = []
    for title in titles:
        titles_list.append(title.text)
    for title in titles_list:
        print(f'Title: {title}')
    contents = soup.find_all('div', {'class': 'entry-content'})
    content_list = []
    for content in contents:
        content_list.append(content.text)
    for content in content_list:
        print(f'Content: {content}')
    f = open("data.csv", "a")
    write_obj = csv.writer(f)
    for text in range(len(content_list)):
        write_obj.writerow([titles_list[text], content_list[text]])
    time.sleep(random.randrange(10, 20))
    f.close()
print('ოპერაცია დასრულებულია, იხილეთ data.csv ფაილი')
