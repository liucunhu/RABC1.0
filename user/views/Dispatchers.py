"""
======================
@author:LCH
@time:2022/4/3:1:06
@email:786608954@qq.com
======================
"""
# --*--encoding:utf-8--*--
from user import models
from django.shortcuts import  render,redirect
from user.utils.permissionUtil import MakeAboutUserSomeThing


# user_infos = models.UserInfo.objects.all()
# role_infos = models.Role.objects.all()
# permissionData = MakeAboutUserSomeThing()
# permissioin_infos = permissionData.get_per_data()
#给用户分配角色及权限
def display_role_per_user_info(request):
    if request.method=='GET':
        user_infos = models.UserInfo.objects.all()
        role_infos = models.Role.objects.all()
        permissionData = MakeAboutUserSomeThing()
        permissioin_infos = permissionData.get_menu_data()
        uid=request.GET.get('uid',None)
        rid=request.GET.get('rid',None)
        user_has_roles=None
        role_has_permission=None
        role_save_btn=None
        permission_save_btn=None
        
        if uid:
            user_info=models.UserInfo.objects.filter(id=uid).first()
            user_has_roles=[ id for value in user_info.roles.values('id') for key,id in value.items()]
            role_save_btn="<input type='submit' value='保存'>"
            print(user_has_roles)
        if rid:
            role_info=models.Role.objects.filter(id=rid).first()
            role_has_permission=[id for value in role_info.permissions.values('id') for key,id in value.items()]
            permission_save_btn="<input type='submit' class='pull-right' value='保存'>"

            print(role_has_permission)
            
        return render(request, 'role_user_per_display.html',
                      {'all_role_info': role_infos,
                       'all_user': user_infos,
                       'permission_infos':permissioin_infos,
                       'uid':uid,'rid':rid,
                       'user_has_role':user_has_roles,
                       'role_save_btn':role_save_btn,
                       'permission_save_btn': permission_save_btn,
                       'role_has_permission':role_has_permission
                       })
    #给用户分配角色



