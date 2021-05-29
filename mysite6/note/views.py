from django.shortcuts import render

# Create your views here.
from  django.http import  HttpResponseRedirect
from django.http import HttpResponse
from user.models import User
from . import models

def check_llogin(fn):
    def wrap(request,*args,**kwargs):
        if not hasattr(request, 'session'):
            return HttpResponseRedirect('/user/login')
        if 'user' not in request.session:
            return HttpResponseRedirect('/user/login')
        return fn(request,*args,**kwargs)
    return wrap

@check_llogin
def list_view(request):
    user_id=request.session['user']['id']
    auser=User.objects.get(id=user_id)
    notes=auser.note_set.all()
    return render(request,'note/show_all.html',locals())

@check_llogin
def add_view(request):
    if request.method=="GET":
        return render(request,'note/add_note.html')
    elif request.method=="POST":
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        user_id=request.session['user']['id']
        auser=User.objects.get(id=user_id)
        anote=models.Note.objects.create(title=title,
                                         content=content,
                                         user=auser)
        return HttpResponseRedirect('/note')

@check_llogin
def mod_view(request,id):
    user_id=request.session['user']['id']
    auser=models.User.objects.get(id=user_id)
    anote=models.Note.objects.get(user=auser,id=id)
    if request.method=="GET":
        return render(request,'note/mod_note.html',locals())
    elif request.method=="POST":
        title=request.POST.get('title','')
        content=request.POST.get('content','')
        anote.title=title
        anote.content=content
        anote.save()
        return HttpResponseRedirect('/note')

@check_llogin
def del_view(request,id):
    user_id = request.session['user']['id']
    auser = models.User.objects.get(id=user_id)
    anote = models.Note.objects.get(user=auser, id=id)
    anote.delete()
    return HttpResponseRedirect('/note')