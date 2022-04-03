# from user.models import UserInfo
from user import models
from user.views import modelsform
from django.views import View
from user.utils.SafetyTool import CiphertextMaker
from django.shortcuts import render,redirect,HttpResponse


#uname ，tname ，pword ，email ，mobile ，roles ，isactive

def get_user_info(request):
    all_user = models.UserInfo.objects.all()
    if request.method=='GET':

        return render(request,'aboutuser.html',{'all_user':all_user})
    else:
        return render(request, 'aboutuser.html', {'all_user': all_user})
def add_edit_user_info(request,uid=None):
    userobj=models.UserInfo.objects.filter(id=uid).first()
    md5_tool = CiphertextMaker()

    if request.method=='GET':
        if userobj:
            user_model_form = modelsform.UserModelForm(instance=userobj)

        else:
            user_model_form = modelsform.UserModelForm()

        return render(request,'edit_add_user.html',{'user_model_form':user_model_form})
    else:
        if userobj:
            save_data=modelsform.UserModelForm(request.POST,instance=userobj)
        else:
            save_data=modelsform.UserModelForm(request.POST)
        if save_data.is_valid():
            user_data = save_data.save(commit=False)
            user_data.pword = md5_tool.make_md5(user_data.pword)
            user_data.save()

            return redirect('umanagelist')
        else:
            return render(request, 'edit_add_user.html', {'user_model_form': save_data})
def delete_user_info(request,uid):

    if request.method=='GET':
        models.UserInfo.objects.filter(id=uid).first().delete()


        return redirect('umanagelist')
    else:
        return redirect('umanagelist')
def start_stop_user(request,uid):
    if request.method == 'GET':
        userobj=models.UserInfo.objects.filter(id=uid).first()
        if userobj.isactive==True:
            userobj.isactive=False
        else:
            userobj.isactive = True
        userobj.save()

        return redirect('umanagelist')
    else:
        return redirect('umanagelist')










