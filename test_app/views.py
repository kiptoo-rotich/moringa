from django.shortcuts import redirect, render
from.models import School
from .forms import SchoolForm

def index(request):
    schools=School.objects.all()
    if request.method=="POST":
        form=SchoolForm(request.POST,request.FILES)
        if form.is_valid():
            school=form.save(commit=False)
            school.user=request.user
            school.save()
            return redirect('home')
    else:
        form=SchoolForm()
    return render(request,'index.html',{'schools':schools,'form':form})

def editschool(request,id):
    schools=School.objects.filter(id=id).first()
    if request.method=="POST":
        form=SchoolForm(request.POST,request.FILES,instance=schools)
        if form.is_valid():
            school=form.save(commit=False)
            school.save()
            return redirect('home')
    else:
        form=SchoolForm(instance=schools)
    return render(request,'editschool.html',{'schools':schools,'form':form})

def deleteschool(request,id):
    school=School.objects.filter(id=id).delete()
    return redirect('home')
