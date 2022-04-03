"""
======================
@author:LCH
@time:2022/3/25:10:28
@email:786608954@qq.com
======================
"""
# --*--encoding:utf-8--*--
from django.shortcuts import render
from django.views import View
from user.utils import DownFontsIcon
def get_fonts(reqeust):
    if reqeust.method=='GET':
        fontDict=DownFontsIcon.get_font_Dict()
        return render(reqeust,'fontsdisplay.html',{'fonts':fontDict})