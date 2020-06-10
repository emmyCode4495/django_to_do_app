from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

def add_task(request):

    task = Task.objects.all() 
    form = TaskForm(request.POST)
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
   
    context = {'task':task,'form':form}
    return render(request,'frontend/index.html',context)


def update_task(request, pk):

    tasks = Task.objects.get(id = pk)
    form = TaskForm(instance = tasks)
    if request.method=="POST":
        form = TaskForm(request.POST, instance = tasks)
        if form.is_valid():
            form.save()
            return redirect("add_task")
        
    context = {"form":form}
    return render(request,'frontend/update.html',context)

def delete_task(request, pk):

    items = Task.objects.get(id = pk)

    if request.method=="POST":
        items.delete()
        return redirect('add_task')
    
    context = {"items":items}
    return render(request,'frontend/delete.html',context)

def about_page(request):
    return render(request,'Registration/about.html')

    
