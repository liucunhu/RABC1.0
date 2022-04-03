"""
======================
@author:LCH
@time:2022/4/1:13:37
@email:786608954@qq.com
======================
"""
# --*--encoding:utf-8--*--
from user import models
# from django.db import models
from collections import OrderedDict
from RABC.settings import (PERMISSION_KEY, MENU_KEY)
'''
'''

class MakeAboutUserSomeThing():
    def __init__(self, islogin=None, request=None):
        self.islogin = islogin
        self.request = request
        self.all_per_list = models.Permission.objects.values('id',
                                                             'title',
                                                             'url',
                                                             'ico',
                                                             'pid_id',
                                                             'menu_id',
                                                             'weight',
                                                             'is_menu',
                                                             'url_name','menu_id__id','menu_id__name','menu_id__ico','menu_id__weight').order_by('-weight')
        self.menu_list = models.Permission.objects.values('id',
                                                             'title',
                                                             'url',
                                                             'ico',
                                                             'pid_id',
                                                             'menu_id',
                                                             'weight',
                                                             'is_menu',
                                                             'url_name','menu_id__id','menu_id__name','menu_id__ico','menu_id__weight').order_by('-menu_id__weight')
    #获取所有的权限信息并返回有序的杼字典供后期生成菜单展示使用
    def get_per_data(self):
        # 'id',
        # 'title',
        # 'url',
        # 'ico',
        # 'pid_id',
        # 'menu_id',
        # 'weight',
        # 'is_menu',
        # 'url_name'

        all_per_dict=OrderedDict()
        # print('permission>>>',models.Permission.objects.values())
        # print('permissionlist>>',self.all_per_list)
        for permission in self.all_per_list:
            #print(permission)
            if permission['menu_id'] :

                all_per_dict[permission['id']]={
                    'id':permission['id'],
                    'title':permission['title'],
                    'url': permission['url'],
                    'is_menu': permission['is_menu'],
                    'pid': permission['pid_id'],
                    'ico': permission['ico'],
                    'menu_id': permission['menu_id'],
                    'weight':permission['weight'],
                    'url_name':permission['url_name'],
                    'children':[]

                }


            else:
                if permission['pid_id'] and permission['pid_id'] in all_per_dict:
                    all_per_dict[permission['pid_id']]['children'].append({ 'id':permission['id'],
                        'title':permission['title'],
                        'url': permission['url'],
                        'is_menu': permission['is_menu'],
                        'pid': permission['pid_id'],
                        'ico': permission['ico'],
                        'menu_id': permission['menu_id'],
                        'weight':permission['weight'],'url_name':permission['url_name']})

       # print(all_per_dict)
        return all_per_dict
    #获取菜单数据
    def get_menu_data(self):
        menu_list=[]
        menu_dict = {}
        for permission in self.menu_list:
            
            if permission['menu_id']:
                if permission['menu_id'] in menu_dict:
                    menu_dict[permission['menu_id']]['children'].append({permission['id']:{'id': permission['id'],
                                                             'title': permission['title'],
                                                             'url': permission['url'],
                                                             'is_menu': permission['is_menu'],
                                                             'pid': permission['pid_id'],
                                                             'ico': permission['ico'],
                                                             'menu_id': permission['menu_id'],
                                                             'weight': permission['weight'],
                                                             'url_name': permission['url_name'],
                                                             'children': []}})
                    
                else:
                    menu_dict[permission['menu_id']] = {'id': permission['menu_id'],
                                                        'title': permission['menu_id__name'],
                                                        'ico': permission['menu_id__ico'],
                                                        'weight': permission['menu_id__weight'],
                                                        'children': [
                                                            {permission['id']: {'id': permission['id'],
                                                                                'title': permission['title'],
                                                                                'url': permission['url'],
                                                                                'is_menu': permission['is_menu'],
                                                                                'pid': permission['pid_id'],
                                                                                'ico': permission['ico'],
                                                                                'menu_id': permission['menu_id'],
                                                                                'weight': permission['weight'],
                                                                                'url_name': permission['url_name'],
                                                                                'children': []}}
                                                        
                                                        ]}
            else:
                for key in menu_dict.keys():
                   for sub in  menu_dict[key]['children']:
                       if permission['pid_id'] in sub:
                           sub[permission['pid_id']]['children'].append(  {permission['id']: {'id': permission['id'],
                                                                                'title': permission['title'],
                                                                                'url': permission['url'],
                                                                                'is_menu': permission['is_menu'],
                                                                                'pid': permission['pid_id'],
                                                                                'ico': permission['ico'],
                                                                                'menu_id': permission['menu_id'],
                                                                                'weight': permission['weight'],
                                                                                'url_name': permission['url_name'],
                                                                                }})
                               
            
        return menu_dict
        
                
                
            







if __name__ == '__main__':
    obj = MakeAboutUserSomeThing(None, None)
    obj.get_per_data()
    print(obj.all_per_list)
