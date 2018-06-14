#coding:utf8
#百度相关搜索关键词挖掘  开发者：李亚涛 wx:841483350
import requests,re,wx,threading,sys
from lxml import etree
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
headers={"Host":"www.baidu.com","User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
def get_html(url):
    while True:
        try:
            html=requests.get(url).content
            return html
        except:
            pass
list=[]
def get_word(word):
    x=word
    list.append(x)
    url='http://www.baidu.com/s?wd=%s'%x
    html=get_html(url)
    # print html
    soup=BeautifulSoup(html,'html.parser')
    data=soup.find_all("div",id="rs")
    if data:
        words=data[0].find_all('a')
        for word in words:
            word=word.text
            if word not in list:
                if '%s'%y in str(word):
                    print word
                    x=threading.Thread(target=get_word,args=(word,))
                    x.start()
                else:
                    continue
            else:
                continue


if __name__=="__main__":
   
    word="减肥"  
    y=word   #y  其实是排除条件，意思是挖掘出的关键词必需包含的关键词
    get_word(word)
