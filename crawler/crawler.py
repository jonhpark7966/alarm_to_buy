#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

class Crawler:
    def find(keyword):
        assert(0); # pure virtual!


class PpCrawler:
    def __init__(self):
        self.url = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'

    def find(self, keyword):

        soup = BeautifulSoup(requests.get(self.url).text, 'html.parser')
        raw_lists = soup.find_all("tr", {"class": "list1"})
        raw_lists.extend(soup.find_all("tr", {"class": "list0"}))

        assert(len(raw_lists) == 20)

        for li in raw_lists:
            title = (li.find("font").text)
            if keyword in title:
                #TODO: do something!
                print(title)
            registered_time = (li.find("nobr", {"class": "eng list_vspace"}).text)
            link = (li.find("td", {"valign":"middle"}).find("a")["href"])
            list_num = li.find("td", {"class", "eng list_vspace"}).text

        return list_num
