from django.shortcuts import render, redirect
from .forms import AddNewProject
from .models import ProjectFormat
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='user_login')
def projects(request):
    all_projects = ProjectFormat.objects.all()
    return render(request, 'projects/project.html', {"all_projects": all_projects})



def add_project(request):
    if request.method == 'POST':
        form = AddNewProject(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('allProjects')
        
    else:
        form = AddNewProject()
    return render(request, 'projects/add_project.html', {'form': form})


def delete_project(request, id):
    oneProject = ProjectFormat.objects.get(id=id)
    if request.method == 'POST':
        oneProject.delete()
        return redirect('allProjects')