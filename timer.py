#!/usr/bin/python3

import sys
import getopt

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

def main():

    # default params for main
    mailSenderId = "abc@gmail.com"
    mailSenderPasswd = "deadbeef"
    mailAddressee = []
    ppKeyword = "상품권"

    # parse arguments
    try:
        opts, args = getopt.getopt(sys.argv[1:], "h", ["MailSenderId=", "MailSenderPasswd=","MailAddressee=", "PpomppuKeyword=", "help"])
    except:
        print(str(err))
        help()
        sys.exit(1)

    for opt, arg in opts:
        if(opt == "--MailSenderId"):
            mailSenderId = arg
            print("Mail Sender: " + mailSenderId)
        elif(opt == "--MailSenderPasswd"):
            mailSenderPasswd = arg
            print("Mail Sender Password: " + mailSenderPasswd)
        elif(opt == "--MailAddressee"):
            mailAddressee.append(arg)
            print("Mail Addressee: " + arg)
        elif(opt == "--PpomppuKeyword"):
            ppKeyword = arg
            print("Ppomppu Keyword: " + ppKeyword)
        elif(opt == "-h") or (opt == "--help"):
            print("Refer Code for Now!")
            sys.exit(1)



    # init PPOMPPU!
    pp = PpCrawler()
    pp_latest = [-1]

    # init mail sender
    m_sender = MailSender(mailSenderId,mailSenderPasswd)
    m_sender.addAddressees(mailAddressee)

    while True:
        found_list = pp.find(ppKeyword)
        filtered_list = filterLatest(pp_latest, found_list)

        # send mail!
        for elm in filtered_list:
            print(elm)
            m_sender.send(elm[1], elm[1])

        sleep(300)


if __name__ == '__main__':
    main()
