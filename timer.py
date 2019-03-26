#!/usr/bin/python3

from time import sleep
from crawler.crawler import PpCrawler

def filterLatest(latest_num, found_list):
    ret = []
    tmp_max = latest_num[0]
    for elm in found_list:
        if elm[0] > latest_num[0]:
            ret.append(elm)
            tmp_max = max([tmp_max,elm[0]])

    latest_num[0] = tmp_max
    return ret


#PPOMPPU!
pp = PpCrawler()
pp_latest = [-1]

while True:
    found_list = pp.find("상품권")
    filtered_list = filterLatest(pp_latest, found_list)

    #for test!
    print(pp_latest)
    for elm in filtered_list:
        print(elm)

    sleep(20)
