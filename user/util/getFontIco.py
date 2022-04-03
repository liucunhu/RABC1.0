# -*- coding:utf-8
"""
@author:liucunhu
@contact:786608954@qq.com
@version:1.0.0
@file:getFontIco.py
@time:2022/3/24  00 08

"""
from bs4 import BeautifulSoup
import requests
from django.utils.safestring import mark_safe

def send_request():

    url='http://www.fontawesome.com.cn/faicons/'
    resp=requests.get(url)
    result=resp.content.decode('utf-8')
    return result

def get_fonts():
    html_doc=send_request()
    soup=BeautifulSoup(html_doc,'html.parser')
    sectionlist=[]
    fontsid=soup.find(id='icons')
    for i in fontsid.find_all('section'):
        
        if i.get('id')=='new':
            
            continue
        sectionlist.append(i.get('id'))

    fontDict = {}
    for section in sectionlist:
        a=[]
        fonts=soup.find(id=section).find_all('i')
        for font in fonts:
            a.append({'name':font.get('class')[1],'htmltag':str(font)})
            print(type(str(font)))
            
        fontDict[section]=a
    return fontDict
    

    
if __name__ == '__main__':
    get_fonts()