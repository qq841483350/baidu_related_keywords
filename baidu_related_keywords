#coding:utf8
#百度相关搜索关键词挖掘，用户搜索关键词拓展，在下方输入一个 关键词 然后回车运行，运行完成后会生成一个以输入关键词命名的文本文件用来存放挖掘好的关键词
import requests,re,time,os,sys
headers={"Host":"www.baidu.com","User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0"}
list=[]
def get_html(keyword):
    x=keyword
    list.append(x)
    url='http://www.baidu.com/s?wd=%s'%x
    html=requests.get(url).content
    html=re.findall('<div id="rs">([\s\S]*?)<div id="page" >',html)[0]
    words=re.findall('<a href="[\s\S]*?">([\s\S]*?)</a>',html)
    for word in words:
        if word not in list:
            if '%s'%y1 in str(word):

                print word.decode('utf8')
                f.write(word+'\n')
                get_html(word)

            else:
                continue

        else:
           continue

if __name__=="__main__":
    print '\n文件运行会自动新建一个keyword.txt的文档，如果同目录下已存在,请清空文档中的内容。\n'.decode('utf8')
    print """<请输入一个关键词如【长沙买房】，按回车，我会自动拓展关键词相关的搜索词>\n""".decode('utf8')
    y=raw_input('enter one word:')
    # y=raw_input(unicode('请输入一个关键词:','utf8').encode('gbk')) #DOS命令


    print """\n<由于挖掘的词可能过多，你可以输入一个限制词，比如挖掘的关键词中必须包含：【买房】，就在下方输入【买房】，然后按回车\n
注：如果不做限制，可以不输入直接按回车>
          """.decode('utf8')

    y1=raw_input('inter the word:')
    # y1=raw_input(unicode('请输入要包含的关键词:','utf8'))  #DOS命令

    f=open('%s.txt'%y1.decode('utf8'),'a+')
    # f=open('keyword.txt','a+')
    get_html(y)
    # get_html(y.decode('utf8'))
    print '关键词挖掘完成,3秒后自动打开挖掘好的关键词，请稍等...'.decode('utf8')
    time.sleep(3)
    f.close()
    os.system('%s.txt'%y.decode('utf8').encode('gbk'))
   
    raw_input('...')
