from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.core.paginator import Paginator, EmptyPage
from .models import List
from .forms import *


def index(request):
    lists = List.objects.all()
    #applying Pagination
    p = Paginator(lists, 5)
    page_number = request.GET.get('page')
    lists = p.get_page(page_number)
    form = ListForm()
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'list': lists,'form':form}
    return render(request,'todo/todo.html',context)



def update(request,pk):
    task = List.objects.get(id=pk)
    form = ListForm(instance=task)
    if request.method == 'POST':
        form = ListForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request,'todo/update.html',context)



def delete(request,pk):
    task = List.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    return render(request,'todo/delete.html')
        

    