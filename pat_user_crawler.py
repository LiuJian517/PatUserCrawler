'''
Author:LiuJian
Date:2017-06-01

技术路线：
1.根据PAT排名页面下载所有用户排名列表（但排名列表显示的为昵称）
2.通过每条数据的当中链接，进入个人主页
3.获取用户名
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
        return ''


# PAT排名页面地址
url_base = "https://www.patest.cn/contests/pat-a-practise/ranklist?page="

# PAT用户主页地址前缀
user_url_base = "https://www.patest.cn"

# 保存获取到的用户名
user = []

def get_user(url):
    html = get(url)
    soup = BeautifulSoup(html,'html.parser')
    # print(soup.prettify())
    
    table = soup.find('tbody')
    for tr in table.children:
        if isinstance(tr,bs4.element.Tag):
            tds = tr('td')
            u = tds[1].find('a').get('href')  # 用户主页地址后缀
            
            user_url = user_url_base + u      # 与前缀拼接成用户主页URL
            content = get(user_url)
            soup = BeautifulSoup(content,'html.parser')
            tb = soup.find('tbody')
            tr = tb.find('tr')
            td = tr.find('td')
            user.append(td.string)            # 第一个td标签当中的内容为：用户名


if __name__=="__main__":
    num = 293  # 当前PAT甲级排名的页数
    for i in range(1,num+1):
        url = url_base + str(i)
        get_user(url)
        print(r"alredy done:{} of {}".format(i,num))
        
    # print(user)
    
    # 将所有用户名存入文件
    with open("PAT_USER.txt",'w') as f:
        for i in user:
            try:
                f.write(i)    
            except:
                continue
            finally:
                f.write("\n")
            
            

