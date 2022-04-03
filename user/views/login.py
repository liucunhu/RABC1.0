from django.shortcuts import render, redirect, reverse
from user import models
from django.views import View
import re

class LoginView(View):
    def get(self, request):
        from server import routes
        routes.get_all_url_dict()
        return render(request, 'ulogin.html')

    def post(self, request):
        uname = request.POST.get('name')
        pwd = request.POST.get('pwd')
        userobj = models.UserInfo.objects.filter(uname=uname, pword=pwd, isactive=True).first()


        if userobj:
            permission = userobj.roles.values('permissions__pid',
                                              'permissions__id',
                                              'permissions__ico',
                                              'permissions__url',
                                              'permissions__is_menu',
                                              'permissions__title', 'permissions__menu_id__id',
                                              'permissions__menu_id__name',
                                              'permissions__url_name',
                                              'permissions__menu_id__ico', 'permissions__weight',
                                              'permissions__menu_id__weight').order_by('-permissions__weight')
            request.session['is_login'] = True
            request.session['permission'] = list(permission)
            url_list = []
            menu_dict = {}
            #print(permission)
            for perobj in permission:
                url_list.append(perobj.get('permissions__url_name'))
                if perobj.get('permissions__menu_id__id') and perobj.get('permissions__is_menu'):
                    if perobj.get('permissions__menu_id__id') in menu_dict:
                        menu_dict[perobj.get('permissions__menu_id__id')]['child'].append(
                            {'title': perobj.get('permissions__title'), 'url': perobj.get('permissions__url'),
                             'weight': perobj.get('permissions__weight')})
                    else:
                        menu_dict[perobj.get('permissions__menu_id__id')] = {
                            'title': perobj.get('permissions__menu_id__name'), \
                            'ico': perobj.get('permissions__menu_id__ico'), \
                            'weight': perobj.get('permissions__menu_id__weight'), \
 \
                            'child': [{'title': perobj.get('permissions__title'), 'url': perobj.get('permissions__url'),
                                       'weight': perobj.get('permissions__weight')}]}

            #request.session['menus'] = menu_dict
            # print(menu_dict)
            permissionDict={}
            for per in permission:
                permissionDict[per.get('permissions__id')]=per


            from collections import OrderedDict
            keys = sorted(menu_dict, key=lambda x: menu_dict[x]['weight'], reverse=True)

            sessionMenuDict = OrderedDict()
            for key in keys:
                sessionMenuDict[key] = menu_dict[key]

            request.session['permission_key']=permissionDict

            request.session['menus'] = sessionMenuDict
            request.session['url_name']=url_list
            #print(sessionMenuDict)
            return redirect('umanagelist')

        else:
            return redirect('ulogin')
