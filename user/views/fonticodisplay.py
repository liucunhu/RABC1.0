# -*- coding:utf-8
"""
@author:liucunhu
@contact:786608954@qq.com
@version:1.0.0
@file:fonticodisplay.py
@time:2022/3/24  00 49

"""
from user.util import getFontIco
from django.shortcuts import render

def get_fonts(request):
    if request.method=='GET':
        fonts=getFontIco.get_fonts()
        print('>>>>',fonts)
        #test={'web-application': [{'name': 'fa-address-book', 'htmltag': <i aria-hidden="true" class="fa fa-address-book"></i>}]
        return render(request,'icon.html',{'fonts':fonts})