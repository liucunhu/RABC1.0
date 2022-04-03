from django.db import models

# Create your models here.
class UserInfo(models.Model):
    uname=models.CharField(verbose_name="用户名",max_length=12)
    tname=models.CharField(verbose_name="姓名",max_length=20)
    pword=models.CharField(verbose_name="密码",max_length=32)
    email=models.CharField(verbose_name="邮箱",max_length=32)
    mobile = models.CharField(verbose_name="手机号", max_length=12)
    roles=models.ManyToManyField(verbose_name="角色",to="Role",blank=True,null=True)
    isactive=models.BooleanField(verbose_name='用户状态',default=True)

    def __str__(self):
        if self.uname:
            return self.uname
        else:
            return self.uname
class Menu(models.Model):
    name=models.CharField(max_length=12)
    weight=models.IntegerField(blank=True,null=True)
    ico=models.CharField(max_length=32)
    def __str__(self):
        return self.name

class Permission(models.Model):
    title=models.CharField(verbose_name="权限名称",max_length=12)
    url = models.CharField(verbose_name="权限路径", max_length=100)
    ico = models.CharField(verbose_name="图标路径", max_length=100,blank=True,null=True)
    pid = models.ForeignKey(verbose_name="父级菜单",to='self',on_delete=models.CASCADE,blank=True,null=True)
    menu_id=models.ForeignKey(to="menu",on_delete=models.CASCADE,blank=True,null=True)
    weight=models.IntegerField(verbose_name='权重',blank=True,null=True)
    is_menu = models.BooleanField(verbose_name="是否为菜单", default=False)
    url_name=models.CharField(verbose_name='别称',max_length=40,unique=True)


    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.url

class Role(models.Model):
    rname=models.CharField(verbose_name='角色名称',max_length=20)
    permissions=models.ManyToManyField(to="Permission",blank=True,null=True)

    def __str__(self):
        if self.rname:
            return self.rname
        else:
            return self.rname


