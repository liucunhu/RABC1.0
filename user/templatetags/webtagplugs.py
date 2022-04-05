from django import template
from django.template.loader import get_template
import re
register=template.Library()
t=get_template('menu.html')


@register.inclusion_tag('menu.html')
def display_menu(request):
    menulist=request.session.get('menus',None)
    if menulist:
        for key,sub_menu in menulist.items():


           for child in  sub_menu.get('child'):
            if re.match(request.path ,child['url'] ):
                child['class']='active'
        return {'menu_list':menulist}
    else:
        return {'menu_list': menulist}
    # return render(request,'menu.html',menulist)


@register.filter
def url_filter(url_name,request):
    if url_name in request.session['url_name']:
        return True
    else:
        return False
@register.simple_tag
def displayrowcolor(role,uid):
    
    if role.id==int(uid):
        
        return 'class=bg-info'
    else:
       
        return None
        