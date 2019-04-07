#!/usr/bin/python3

from time import sleep
from crawler.crawler import PpCrawler
from alarm.mail_sender import MailSender

# NOTES: each elements of found_list should have "list number, title, link"
def filterLatest(latest_num, found_list):
    ret = []
    tmp_max = latest_num[0]
    for elm in found_list:
        if elm[0] > latest_num[0]:
            ret.append(elm)
            tmp_max = max([tmp_max,elm[0]])

    latest_num[0] = tmp_max
    return ret



#####################
#       MAIN!       #
#####################


# init PPOMPPU!
pp = PpCrawler()
pp_latest = [-1]

# init mail sender
m_sender = MailSender()
m_sender.addAddressees(['jonhpark7966@gmail.com'])

while True:
    found_list = pp.find("상품권")
    filtered_list = filterLatest(pp_latest, found_list)

    # send mail!
    for elm in filtered_list:
        print(elm)
        m_sender.send(elm[1], elm[1])

    sleep(300)
