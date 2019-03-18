#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

html = requests.get('http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu').text

soup = BeautifulSoup(html, 'html.parser')

raw_lists = soup.find_all("tr", {"class": "list1"})
raw_lists.extend(soup.find_all("tr", {"class": "list0"}))

assert(len(raw_lists) == 20)

for li in raw_lists:
    title = (li.find("font").text)
    if "상품권" in title:
        #TODO: do something!
        print(title)
    registered_time = (li.find("nobr", {"class": "eng list_vspace"}).text)
    link = (li.find("td", {"valign":"middle"}).find("a")["href"])
    list_num = li.find("td", {"class", "eng list_vspace"}).text
    print(list_num)
