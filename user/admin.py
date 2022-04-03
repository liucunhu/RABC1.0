from django.contrib import admin
from user import models
# Register your models here.


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['uname','tname' ,'pword' ,'email','mobile' ,'roles','isactive']
    list_editable = ['uname','tname' ,'pword' ,'email','mobile' ,'roles','isactive']
class RoleAdmin(admin.ModelAdmin):
    pass
class PermissionAdmin(admin.ModelAdmin):
    list_display = ['id','title','url','ico','pid','menu_id','is_menu','weight','url_name']
    list_editable = ['title','url','ico','pid','menu_id','is_menu','weight','url_name']
class MenuAdmin(admin.ModelAdmin):
    list_display = ['id','name','ico','weight']
    list_editable = ['name','ico','weight']
admin.site.register(models.UserInfo)
admin.site.register(models.Role)
admin.site.register(models.Permission,PermissionAdmin)
admin.site.register(models.Menu,MenuAdmin)
