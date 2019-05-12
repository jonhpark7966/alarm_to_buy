#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

from selenium import webdriver


class Crawler:
    url_ = ""
    found_list_ = []

    def setUrl(self, url):
        url_ = url

    def find(self, keryword):
        pass

# NOTES: found_list_ consists of "list number (int)", "title", "link"
# USAGE: just call "find(KEYWORD)"
class PpCrawler(Crawler):
    def __init__(self):
        self.url_ = 'http://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu'
        self.found_list_ = []

    def find(self, keyword):
        self.found_list_ = []

        soup = BeautifulSoup(requests.get(self.url_).text, 'html.parser')
        raw_lists = soup.find_all("tr", {"class": "list1"})
        raw_lists.extend(soup.find_all("tr", {"class": "list0"}))

        assert(len(raw_lists) == 20)

        for li in raw_lists:
            title = (li.find("font").text)
            #registered_time = (li.find("nobr", {"class": "eng list_vspace"}).text)
            link = (li.find("td", {"valign":"middle"}).find("a")["href"])
            list_num = li.find("td", {"class", "eng list_vspace"}).text
            if keyword in title:
                self.found_list_.append([int(list_num), title, link])
        return self.found_list_

class WemakepriceCrawler(Crawler):
    def __init__(self):
        return

    def find(self, keyword):
       driver = webdriver.Chrome('./chromedriver')
       driver.get('https://www.naver.com')
