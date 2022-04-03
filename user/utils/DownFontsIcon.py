"""
======================
@author:LCH
@time:2022/3/24:10:25
@email:786608954@qq.com
======================
"""
# --*--encoding:utf-8--*--
import requests
from django.utils.safestring import mark_safe
from bs4 import BeautifulSoup

def get_html_doc():
    try:
        url='https://fontawesome.dashgame.com/'
        resp=requests.get(url)
        return resp.content.decode('utf-8')
    except Exception as e:
        print('请求失败请检查目标服务是否正常',e)
        return None

def get_font_Dict():

    html_doc=get_html_doc()
    if html_doc:
        soup=BeautifulSoup(html_doc,'html.parser')
        new=soup.find(id='new')
        sections=new.findNextSibling('div').findAll('section')

        fontDict=[]
        for section in sections:
            ids=section.get('id',None)
            if ids:
                fonts=soup.find(id=ids)
                fontname=fonts.findChild().text
              
                for ico in fonts.findAll('i'):
                    name=' '.join(ico.get('class'))
                    icotag=mark_safe(str(ico))
                    
                    fontDict.append([name,icotag])
                    

        #print('test>>>',fontDict)
        return fontDict
    else:
        print('未获取到相应的html文件')
        return None


if __name__ == '__main__':
    get_font_Dict()