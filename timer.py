#!/usr/bin/python3

from time import sleep
from crawler.crawler import PpCrawler

#PPOMPPU!
pp = PpCrawler()

while True:
    pp.find("상품권")
    sleep(5)
