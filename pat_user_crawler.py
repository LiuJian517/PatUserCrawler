import requests
from bs4 import BeautifulSoup
import bs4

def get(url):
    try:
        # r = requests.get("http://www.baidu.com")
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ''



url_base = "https://www.patest.cn/contests/pat-a-practise/ranklist?page="

user_url_base = "https://www.patest.cn"
user = []

def get_user(url):
    html = get(url)
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.prettify())

    # urls = []
    table = soup.find('tbody')
    for tr in table.children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            u = tds[1].find('a').get('href')
            
            user_url = user_url_base + u
            content = get(user_url)
            soup = BeautifulSoup(content,'html.parser')
            tb = soup.find('tbody')
            tr = tb.find('tr')
            td = tr.find('td')
            user.append(td.string)


if __name__=="__main__":
    num = 293
    for i in range(1,num+1):
        url = url_base + str(i)
        get_user(url)
        print(r"alredy done:{} of {}".format(i,num))
    # print(user)
    with open("PAT_USER.txt",'w') as f:
        for i in user:
            try:
                f.write(i)    
            except:
                continue
            finally:
                f.write("\n")
            
            

