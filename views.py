from django.shortcuts import render,redirect
from .models import Student
from .forms import studentform
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    return render(request,'home.html',{'name':'Ananthu','college':'DGVC'})
def aboutpage(request):
    return render(request,'aboutus.html')
def getstudents(request):
    students=Student.objects.all()
    return render(request,'students.html',{'students':students})
@login_required(login_url='login')
def addStudent(request):
    form=studentform()
    if request.method=='POST':
        form=studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request,'studentform.html',{'form':form})
@login_required(login_url='login')
def editStudent(request,id):
    stu=Student.objects.get(id=id)
    form=studentform(instance=stu)
    if request.method=='POST':
        form=studentform(request.POST,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request,'studentform.html',{'form':form})
@login_required(login_url='login')
def deleteStudent(request,id):
    stu=Student.objects.get(id=id)
    stu.delete()
    return redirect('students')
def registerPage(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,'register.html')
def loginPage(request):
    form=AuthenticationForm()
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')
    return render(request,'login.html',{'form':form})

def logoutPage(request):
    logout(request)
    return redirect('home')




