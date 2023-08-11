from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse 
import markdown

from django.contrib.messages import constants as messages


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    #   output=util.get_entry(title)
      output=markdown.markdown(util.get_entry(title))
      
      return HttpResponse(output)
def search(request):
     list=[]
     if request.method =='GET':
           

           title=request.GET.get('enter')
           if title in util.list_entries():
        
            # return HttpResponseRedirect(f'wiki/{title}')
            return HttpResponseRedirect(reverse("entry", args=(title,)) )
           
           else:
                if title not in util.list_entries():
                        
                    for entry in util.list_entries():
                        if entry.__contains__(title):
                            list.append(entry)
                
                return render(request, "Encyclopedia/search_result.html", {"list":list} )

def create_page(request):

    return render(request,"Encyclopedia/new_page.html")
    
def save_page(request):
    if request.method =='POST':
            title=request.POST.get('title')
            content=request.POST.get('content')
            if title not in util.list_entries():
                util.save_entry(title ,content)  
                # return HttpResponse(content)
                return HttpResponseRedirect(reverse("entry", args=(title,)) )
            else:
                 messages.ERROR
def edit_page(request, title):
    output=markdown.markdown(util.get_entry(title))
      
    return render(request,'Encysclopeia/edit_page.html',{"output":output})
    #  pass
     