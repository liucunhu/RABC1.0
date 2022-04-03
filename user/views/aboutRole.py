from user import models
from django.views import View
from django.shortcuts import render,redirect,HttpResponse
from user.views.modelsform import RoleModelForm
# class RoleView(View):
#     def get(self,request):
#         rolelist=models.Role.objects.all()
#         return render(request,'rolepage.html',{'rolelist':rolelist})
#     def post(self,request):
#         return HttpResponse('ok')

def get_role_info(request,rid=None):
    all_user=models.UserInfo.objects.all()
    if rid:
        query_role_date=models.Role.objects.filter(id=rid)
        if query_role_date:
            all_role_info=RoleModelForm(instance=query_role_date)
        else:
            all_role_info = models.Role.objects.all()
    else:
        all_role_info=models.Role.objects.all()
    return render(request,'rolepage.html',{'rolelist':all_role_info,})
def add_edit_role_info(request,rid=None):

    roleobj = models.Role.objects.filter(id=rid).first()
    print(models.Role.objects.values())
    print(rid,roleobj)
    if request.method=='GET':
        if roleobj:
            role_info_form=RoleModelForm(instance=roleobj)


        else:
            role_info_form=RoleModelForm()

        return render(request, 'edit_add_role.html', {'role_model_form': role_info_form})
    else:
        if roleobj:
            save_data=RoleModelForm(request.POST,instance=roleobj)
        else:
            save_data = RoleModelForm(request.POST)
        if save_data.is_valid():
            save_data.save()
            return redirect('rolelist')
        else:
            return render(request, 'edit_add_role.html', {'role_model_form': save_data})




def remove_role_info(request,rid):
    if rid:
        if request.method=='GET':
            models.Role.objects.filter(id=rid).first().delete()
            return redirect('rolelist')
        else:
            return HttpResponse('无效的操作')
    else:
        return HttpResponse('非法传参')
