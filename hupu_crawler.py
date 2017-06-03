'''
Author:LiuJian
Date:2017-06-01

看到这位JR做得不错，自己也做了一下
https://bbs.hupu.com/19353218.html

'''
import requests
from bs4 import BeautifulSoup
import bs4

def get(url):
    '''
    根据页面URL下载内容
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        print("ERROR!")
        return ''


def get_user(url):
    html = get(url)
    soup = BeautifulSoup(html,'html.parser')
    # print(soup)
    divs  = soup.find_all('div',"floor_box")
    print(len(divs))

    for div in divs:
        if isinstance(div,bs4.element.Tag):
            h = div.find('a').get('href')
            print(h)

    
if __name__=="__main__":
    url = "https://bbs.hupu.com/19353218-19.html"
    get_user(url)
   
            
            

