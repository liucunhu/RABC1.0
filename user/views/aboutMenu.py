from user import models
from django.views import View
from django.shortcuts import render,redirect,HttpResponse
from user.views import modelsform


class MenuView(View):
    def get(self,request):
        menulist=models.Menu.objects.all()
        return render(request,'aboutmenu.html',{'menulist':menulist})
    def post(self,request):
        return HttpResponse('ok')
    
def getMenuList(request):
    menulist = models.Menu.objects.all()
    return render(request, 'aboutmenu.html', {'menulist': menulist})
def edit_add_menu(request,mid=None):
    menuModelForm=modelsform.MenuModelForm
    mobj = models.Menu.objects.filter(id=mid).first()
    if request.method=='GET':
        if mid:
            menuModelForm=menuModelForm(instance=mobj)
            # fonts = DownFontsIcon.get_font_Dict()
            #print(fonts)
            return render(request,'editMenu.html',{'disalpayMenu':menuModelForm})
        else:
            return render(request,'editMenu.html',{'disalpayMenu':menuModelForm})
    else:
        #saveData = menuModelForm(request.POST)
       
        saveData=menuModelForm(request.POST,instance=mobj)
        
       
        if saveData.is_valid():
            #print('>>>',saveData)
            saveData.save()
            return redirect('permissionlist')
        else:
            return HttpResponse('保存失败')
   
def delete_menu(request,mid):
    if request.method=='GET':
        if mid:
            models.Menu.objects.filter(id=mid).first().delete()
            return redirect('permissionlist')
        else:
            return HttpResponse('缺少必要的参数无法删除')
    else:
        return redirect('permissionlist')
    
        
            
    
    