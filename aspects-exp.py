# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as bs
import requests
import time
import hashlib
import sys
def expp():
    reload(sys)
    sys.setdefaultencoding('utf8')
    f = open("cs.txt","r")
    url=f.readlines()
    for i in url:
        try:
            r=requests.get(i,timeout=5)
            if r.status_code == 200:
                soup=bs(r.text,"html.parser")
                if hashlib.md5:
                    mb1=soup.find_all(name="div",attrs={"class":"line1"})[0].text#获取line1数据
                    mb2=soup.find_all(name="div",attrs={"class":"line2"})[0].text#获取line2数据
                    with open("cs2.txt", "ab") as ft:
                        ft.write(i+"\n"+mb2+"\n"+ mb1)
                        print "\n"+mb1+"\n"+mb2 + "\n" +i

        except:
             pass
    f.close()
expp()
