from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect,HttpResponse
import re
class AuthMiddleware(MiddlewareMixin):

    def process_request(self,request):
        white_list=[reverse('ulogin'),'/admin/.*?',reverse('fontslist')]
        request.cur_id=None

        for  path in white_list:


            result=re.match(path,request.path)
            try:
                pass
                #print('result=',result.group())
            except Exception as e:
                print(e)
            if result:
                return



        # print(re.match('admin',request.path))
        # if re.match('/admin/',request.path):
        #     return
        is_login=request.session.get('is_login',None)
        permission=request.session.get('permission',None)
        #print(f'middle={permission}')
        #print(f'path={request.path}')
        if 1:
            reg=request.path
            
            for path in request.session.get('permission',None):
                #print('>>',request.path,path['permissions__url'])
                if re.match(path['permissions__url'],reg):
                   
                    sessionMenuDict = request.session.get('menus')
                    print('menu>>',sessionMenuDict)
                    for key, value in sessionMenuDict.items():

                        value['class'] = 'hidden'

                        for i in value['child']:
                            #print(request.path, i['url'])
                            if re.match(i['url'],request.path):
                                value['class'] = ''
                                i['class'] = 'active'
                    #return

                    request.breadcrumb =[
                        {'url': 'javascript:void(0)', 'title': '主页'},

                    ]
                    permissionDict = request.session.get('permission_key')
                    print('breadcrumb',permissionDict)
                    #print('>>>', permissionDict)
                    for perInfo in permissionDict.values():
                        #print(perInfo)
                        urls = perInfo['permissions__url']
                       
                        strs = r'^%s$' % urls
                        #print(strs, request.path)
                        if re.match(urls, request.path):
                            #print(strs,request.path)
                            pid = perInfo['permissions__pid']
                            if pid:
                                request.cur_id = pid
                                request.breadcrumb.append({
                                    'url': permissionDict[str(pid)]['permissions__url'],
                                    'title': permissionDict[str(pid)]['permissions__title']
                                })
                                request.breadcrumb.append({
                                    'url': None,
                                    'title': perInfo['permissions__title']
                                })

                            else:
                                request.breadcrumb.append({
                                    'url': None,
                                    'title': perInfo['permissions__title']
                                })
                                request.cur_id=perInfo.get('permissions__id')
                      
                            
                        
                       
                    #print(request.breadcrumb)
                    
            return
        
            
        else:
            return

