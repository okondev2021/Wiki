from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

import markdown2

from markdown2 import markdown

import re


import random
 

def search(request):
    sections=util.list_entries()
    b=[]
    if request.method =='GET':
        find=request.GET['q']  
        if 1 > 0:
            for get in sections:
                if find in sections:
                    page=util.get_entry(find)
                    pages =markdown(page)
                    return render(request,'encyclopedia/search.html',{'entryy': pages})
                elif find.lower() in get.lower():
                    b.append(get)
                    return render(request,'encyclopedia/result.html',{'name':b})


    return render(request,'encyclopedia/error.html',{'error':find})

def index(request):
    return render(request, "encyclopedia/index.html", {"entries":util.list_entries()})

def wikip(request,name):
    if name in util.list_entries():
        global jedi
        jedi=name
        page=util.get_entry(jedi)
        pages =markdown(page)
    else:
        return render(request,"encyclopedia/error.html",{'error':name} )
    return render(request,'encyclopedia/wikip.html',{'entryy': pages })

def error(request):
    return render(request,"encyclopedia/error.html")

def result(request):
    return render(request,"encyclopedia/result.html")

def create(request):
    if request.method =='POST':
        title = request.POST['title']
        content=request.POST['content']
        entries = util.list_entries()
        if title =="" or content =="":
            return render(request,"encyclopedia/create.html")
        if title in entries:
            messages.info(request,f'{title} already exists')
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse("index")) 
    return render(request,"encyclopedia/create.html")

def rando(request):
    randy=random.choice(util.list_entries())
    if randy in util.list_entries():
        page=util.get_entry(randy)
        pages =markdown(page)
    return render(request,'encyclopedia/random.html',{'entryy':pages})

def edit(request):
    check=util.get_entry(jedi)
    if request.method=='POST':
        article=request.POST['write']
        util.save_entry(jedi,article)
        return HttpResponseRedirect(reverse("index")) 
    return render(request,'encyclopedia/edit.html',{'link':check})
