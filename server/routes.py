from RABC import settings
from django.urls import URLResolver,URLPattern
from django.utils.module_loading import import_string,import_module,importlib_find

#from django.urls import URLResolver, URLPattern
import re
from RABC import urls
from collections import OrderedDict
import sys
def get_all_urls(pre_namesapce,pre_url,partterns,all_url_dict):
    #datas=[<URLResolver <URLPattern list> (admin:admin) 'admin/'>, <URLResolver <module 'user.urls' from 'D:\\myfile\\django_project\\RABC\\user\\urls.py'> (None:None) 'umanage/'>]
    namespace=None
    for items in partterns:
        if isinstance(items,URLPattern):
            if pre_namesapce:
                if items.name:
                    name='%s:%s' %(pre_namesapce,items.name)
                else:
                    name=pre_namesapce
            else:
                if items.name:
                    name=items.name
                else:
                    raise Exception('name属性不能为空')
            all_url_dict[name]={'url_name':name,'url':pre_url+str(items.pattern)}
        elif isinstance(items,URLResolver):
            if pre_namesapce:
                if items.namespace:
                    namespace='%s:%s' %(pre_namesapce,items.namespace)
                else:
                    namespace=pre_namesapce
            else:
                if items.namespace:
                    namespace=items.namespace
                else:
                    namespace=None

            get_all_urls(namespace,pre_url+str(items.pattern),items.url_patterns,all_url_dict)


def get_all_url_dict(igore_namesapce_list=None):
    igore_list=igore_namesapce_list or []
    path=settings.ROOT_URLCONF
    datas=import_string(path).urlpatterns
    all_url_dict=OrderedDict()
    allpatterns=[]
    for items in datas:
        if isinstance(items,URLResolver) and items.namespace in (igore_list):
            continue
        allpatterns.append(items)

    get_all_urls(None,"/",allpatterns,all_url_dict)
    #print(all_url_dict)

    return all_url_dict

if __name__ == '__main__':
    get_all_url_dict()