# -*- coding: utf-8 -*-
import re
import requests
import time
import lxml.html
from bs4 import BeautifulSoup

def getSalary(url):

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

    resp=requests.get(url,headers=headers)

    time.sleep(5)

    web_data = BeautifulSoup(resp.content, "lxml")

    firstlist=web_data.find_all('td')

    salarylist1=[]

    salarylist2=[]

    for i in firstlist:

        if 'zwyx' in str(i) and 'mian yi' not in str(i):

            salarylist1.append(str(i))
    salaryliststr='+'.join(salarylist1)

    reeq=re.compile(r'(\w[0-9]+)\w*')

    salarylist2=re.findall(reeq,salaryliststr)

    salarylist2=map(float,salarylist2)

    return salarylist2

def getAverageSalary(keyword):

    url=r'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E5%8C%97%E4%BA%AC&kw='+keyword+'&sm=0&p=1&kt=3'

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}

    pagelist=[]

    salarylist=getSalary(url)

    print salarylist

    while True:

        resp=requests.get(url,headers=headers)

        time.sleep(5)

        if resp.status_code!=200:

            break

        resp=resp.content

        reg=r'a href="(.*?)" class="next-page">next page</a>'

        reg=re.compile(reg)

        page=re.findall(reg,resp)

        if page!=[]:

            page1=re.split(r'href="',page[0])

            if re.search('http',page1[-1]):

                pagelist.append(page1[-1])

                url=page1[-1]

                salarylist2=getSalary(url)

                #print 'salarylist',salarylist

                salarylist.extend(salarylist2)

                #print 'salarylist2',salarylist

            else:

                break

        else:

            break

    salarylist=map(float,salarylist)

    if len(salarylist)!=0:

        averageSalary=sum(salarylist)/len(salarylist)

        return averageSalary,pagelist

    else:

        print 'the result is zero, please check the website'

        return 0,[0,]



averageSalary,pagelist=getAverageSalary('CAE')

print 'AverageSalary:',averageSalary