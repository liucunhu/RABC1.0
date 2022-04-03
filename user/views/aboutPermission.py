import re

from user import models
from django.views import View
from django.shortcuts import render, redirect, reverse, HttpResponse
from user.views import modelsform
from django.forms.models import modelformset_factory, formset_factory

from server import routes
from user.utils.permissionUtil import MakeAboutUserSomeThing

class PermissionView(View):
    form_class = modelsform.PermissionForm
    initial = {'key': 'value'}

    def get(self, request):
        menulist = models.Menu.objects.all()
        allPermissionDict = {}
        mid = request.GET.get('mid', None)
        typemethod = request.GET.get('methodtype', None)
        # print(typemethod,mid)
        # if typemethod and typemethod=='add':
        #     form = self.form_class(initial=self.initial)
        #     return render(request, 'addPermission.html', {'form': form})
        # else:
        if mid:

            allPermission = self.get_all_permission_dict()
            for key, permission in allPermission.items():
                # print(permission['menu_id_id'],type(permission['menu_id_id']))
                if permission['menu_id'] == int(mid):
                    allPermissionDict[key] = permission
                    # allPermissionDict[key]=permission[key]

        else:
            allPermissionDict = self.get_all_permission_dict()

        return render(request, 'permissonpage.html', {'perlist': allPermissionDict, 'menulist': menulist})

    def post(self, request, *args, **kwargs):
        pass

    def get_all_permission_dict(self):
        permissionlist = models.Permission.objects.values()
        perobjs=MakeAboutUserSomeThing()


        allPermissionDict = perobjs.get_per_data()

        return allPermissionDict


# def addPermission(request):
#     form_class = modelsform.PermissionForm
#     if request.method=='POST':
#         form = form_class(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('permissionlist')
#     elif request.method=='GET':
#         permissionId=request.GET.get('persid',None)
#         if permissionId:
#             obj=models.Permission.objects.filter(id=permissionId).first()
#             form_class=modelsform.PermissionForm(instance=obj)
#             return render(request, 'addPermission.html', {'form': form_class})
#         else:
#             return render(request, 'addPermission.html', {'form': form_class})

def addPermission(request, perid=None):
    form_class = modelsform.PermissionForm
    perobj = models.Permission.objects.filter(id=perid).first()
    if request.method == 'GET':
        if not perobj:

            return render(request, 'addPermission.html', {'form': form_class})
        else:
            form_class = modelsform.PermissionForm(instance=perobj)
            return render(request, 'addPermission.html', {'form': form_class})
    else:
        if re.match(reverse('permission_edit'), request.path):
            form_class = modelsform.PermissionForm(request.POST, instance=perobj)
        else:
            form_class = modelsform.PermissionForm(request.POST)
        if form_class.is_valid():
            form_class.save()
            return redirect('permissionlist')


def deletePermission(request, perid):
    if request.method == 'GET':
        models.Permission.objects.filter(id=perid).first().delete()
        return redirect('permissionlist')


def addmulPermission(request):
    per_modelform_set = modelformset_factory(models.Permission, modelsform.MulPermission, extra=0)
    all_per_data = models.Permission.objects.all()
    add_formset = formset_factory(modelsform.MulPermission, extra=0)
    ignore_list = ['admin']
    routers_all = routes.get_all_url_dict(ignore_list)
    # print(routers_all)
    router_all_set = set(list(routers_all.keys()))
    # print(router_all_set)
    data_url_set = set([i.url_name for i in all_per_data])
    add_url_name = router_all_set - data_url_set
    # print(add_url_name)
    add_moderset = add_formset(initial=[row for name, row in routers_all.items() if name in add_url_name])
    # print([row for name,row in routers_all.items() if name in add_url_name])
    del_url_name = data_url_set - router_all_set

    del_moderset = per_modelform_set(queryset=models.Permission.objects.filter(url_name__in=del_url_name))
    update_url_name = data_url_set & router_all_set

    update_moderset = per_modelform_set(queryset=models.Permission.objects.filter(url_name__in=update_url_name))
    # print(update_url_name)
    method_type = request.GET.get('type', None)
    #print(method_type)
    if request.method == 'GET' and method_type == None:
        a=MakeAboutUserSomeThing(request,True)
        a.get_per_data()
        return render(request, 'edit_add_mul_permission.html',
                      {'add_form_set': add_moderset,
                       'edit_formset': update_moderset, 'del_formset': del_moderset})

    elif request.method == 'POST' and method_type == 'add':
        save_data = add_formset(request.POST)
        if save_data.is_valid():
            #print('合规数据', save_data.cleaned_data)
            save_data_list = [models.Permission(**i) for i in save_data.cleaned_data]
            models.Permission.objects.bulk_create(save_data_list)
            return redirect('muladdpermission')
        else:
            #print(save_data.errors)
            return render(request, 'edit_add_mul_permission.html',
                          {'add_form_set': add_moderset,
                           'edit_formset': update_moderset, 'del_formset': del_moderset})
    elif method_type == 'delete':
        delete_url = request.GET.get('id', None)
        #print('id=', delete_url)
        if delete_url:
            del_obj = models.Permission.objects.filter(id=delete_url).first()
            if del_obj:

                del_obj.delete()
                return redirect('muladdpermission')
            else:

                return HttpResponse('未找到需要删除的数据')
        else:
            return HttpResponse('参数传递错误')
    elif request.method == 'POST' and method_type == 'update':
        save_modelform_set = modelformset_factory(models.Permission, modelsform.MulPermission, extra=0)

        update_data = save_modelform_set(request.POST)
        # print('updatedata=',request.POST)
        if update_data.is_valid():
            #update_list = [models.Permission(**i) for i in update_data.cleaned_data]
            # #print('data=',update_data)
            # print(update_data.cleaned_data)
            list_filed = ['title', 'url', 'pid', 'menu_id', 'url_name']
            update_data.save()
            return redirect('muladdpermission')

        else:
            # #print(update_data.error_messages,
            #       '\n secondmesson', update_data.errors, '\n', update_data.non_form_errors())
            return render(request, 'edit_add_mul_permission.html',
                          {'add_form_set': add_moderset,
                           'edit_formset': update_moderset, 'del_formset': del_moderset})
    else:
        return render(request, 'edit_add_mul_permission.html',
                      {'add_form_set': add_moderset,
                       'edit_formset': update_moderset, 'del_formset': del_moderset})
