"""liucunhu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path
from user import views

from user.views import aboutRole
from user.views import aboutuser
from user.views.login import LoginView
from user.views.aboutPermission import PermissionView
from user.views.aboutMenu import (MenuView, edit_add_menu, delete_menu)
#from user.views.views import get_fonts
from user.views.aboutPermission import addPermission
from user.views.aboutPermission import deletePermission
from user.views.aboutPermission import addmulPermission
from user.views import Dispatchers
'''
/customer/add/
/customer/delete/
/customer/list/
/customer/edit/
/payment/add/
/payment/refound/
/payment/edit/
/payment/list/

'''

urlpatterns = [

    # path('login/', auth.login,name='login'),
    # path('index/', auth.index,name='index'),
    # path('customer/add/', customer.customeradd,name='customeradd'),
    # path('customer/delete/', customer.customerdelete,name='customerdelete'),
    # path('customer/list/', customer.customerlist,name='customerlist'),
    # path('customer/edit/', customer.customeredit,name='customeredit'),
    # path('payment/add/', payment.paymentadd,name='paymentadd'),
    # path('payment/refound/', payment.paymentrefound,name='paymentrefound'),
    # path('payment/list/', payment.paymentlist,name='paymentlist'),
    # path('payment/edit/', payment.paymentedit,name='paymentedit'),
    path('userlist/',aboutuser.get_user_info,name='umanagelist'),
    path('user/add',aboutuser.add_edit_user_info,name='adduser'),
    re_path(r'user/edit/(\d+)',aboutuser.add_edit_user_info,name='edituser'),
    re_path(r'user/delete/(\d+)',aboutuser.delete_user_info,name='deluser'),
    re_path(r'user/stuser/(\d+)',aboutuser.start_stop_user,name='userstart'),
    path('ulogin/',LoginView.as_view(),name='ulogin'),
    re_path(r'^role/list',aboutRole.get_role_info,name='rolelist'),
    re_path(r'^role/add/',aboutRole.add_edit_role_info,name='roleadd'),
    re_path(r'^role/edit/(\d+)/',aboutRole.add_edit_role_info,name='roleedit'),
    re_path(r'^role/del/(\d+)',aboutRole.remove_role_info,name='roledel'),
    path('permissionlist/', PermissionView.as_view(), name='permissionlist'),
    re_path(r'^dispatcherslist/',Dispatchers.display_role_per_user_info,name='displaydispachers'),
    # re_path(r'^dispatchersrole/',Dispatchers.dispacherRole,name='dispacher_role'),
    # re_path(r'^dispatcherspermission/',Dispatchers.dispacherPermission,name='dispacher_permission'),

    path('permissionadd/', addPermission, name='permissionadd'),
    re_path(r'permissionedit/(\d+)', addPermission, name='permission_edit'),
    # re_path(r'permissionedit/', addPermission, name='permission_edit'),
    re_path(r'permissiondelete/(\d+)', deletePermission, name='permission_del'),
    re_path(r'muladdPermission/',addmulPermission,name='muladdpermission'),
    path('menulist/', MenuView.as_view(), name='menulist'),
    re_path('menuedit/(\d+)',edit_add_menu, name='menu_edit'),
    re_path('menuadd/',edit_add_menu, name='menu_add'),
    re_path(r'menudelete/(\d+)',delete_menu, name='menu_del'),

    #path('fonts/', get_fonts, name='fontslist'),

]
