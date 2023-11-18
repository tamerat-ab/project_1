from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse 
import markdown
import random

from django.contrib.messages import constants as messages


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    try:
        output=markdown.markdown(util.get_entry(title)) 
        return HttpResponse(output)
    except:
       return HttpResponse('the requested page does not exist')
      
def search(request):
     list=[]
     if request.method =='GET':
           

           title=request.GET.get('enter')
           if title.lower() in [x.lower() for x in util.list_entries()]:
        
            # return HttpResponseRedirect(f'wiki/{title}')
            return HttpResponseRedirect(reverse("entry", args=(title,)) )
           
           else:
                if title not in util.list_entries():
                        
                    for entry in util.list_entries():
                        if entry.lower().__contains__(title.lower()):
                            list.append(entry)
                
                return render(request, "Encyclopedia/search_result.html", {"list":list} )

def create_page(request):

    return render(request,"Encyclopedia/new_page.html")
    
def save_page(request):
    if request.method =='POST':
            title=request.POST.get('title')
            content=request.POST.get('content')
            if title.lower() not in [x.lower() for x in util.list_entries()]:
                util.save_entry(title ,content)  
                # return HttpResponse(content)
                return HttpResponseRedirect(reverse("entry", args=(title,)) )
            else:
                return render (request,'Encyclopedia/new_page.html',{'message':'The title already exists'})

def edit_page(request, title):
    if title:
        output=markdown.markdown(util.get_entry(title))
        
        return render(request,'Encyclopedia/edit_page.html',{"output":output ,"title":title})
def save_change(request):

    if request.method =='POST':
            title=request.POST.get('title')
            content=request.POST.get('content')
            util.save_entry(title ,content)  
            return HttpResponseRedirect(reverse("entry", args=(title,)) )

def random_page(request):
     entry=util.list_entries()
     random_entry=random.choice(entry)
     return HttpResponseRedirect(reverse("entry", args=(random_entry,)) )

    #  return render(request,'Encyclopedia/random_page.html',{"random_entry":random_entry})
              