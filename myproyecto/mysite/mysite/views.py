from django.shortcuts import render



from django.core import serializers

from myapp.models import Projects

data = serializers.serialize("python", Projects.objects.all())



context = {
    "data": data
}



def home(request):
    # projects = Projects.objects.all()

    return render(request, 'index.html',context)
    
    #return render(request, 'index.html', {
       # "projects" : projects;
    #})

def home2(request):
    return render(request, 'canaima.html',context)

def home3(request):
    return render(request, 'humboldt.html',context)

def home4(request):
    return render(request, 'morrocoy.html',context)

def manager_detail(request, manager_name):
    projects = Projects.objects.filter(manager_name=manager_name)
    context = {
        "projects": projects
    }
    return render(request, 'manager_detail.html', context)

"""



def home(request):
    # projects = Projects.objects.all()

    return render(request, 'index.html')
    
    #return render(request, 'index.html', {
       # "projects" : projects;
    #})

def home2(request):
    return render(request, 'canaima.html')

def home3(request):
    return render(request, 'humboldt.html')

def home4(request):
    return render(request, 'morrocoy.html')
"""




