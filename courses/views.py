from django.shortcuts import render,redirect, get_object_or_404
from .models import course
from .forms import courseForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.utils import timezone

# Create your views here.
def courses(request):
    if request.user.typeof=='teacher':
        courses=course.objects.filter(id_teacher=request.user)

        return render(request,'project/CoursesPage.html',{'courses':courses})
    else:
        
        return render(request,'project/CoursePage2.html')

def courseslist(request):
    if request.user.typeof=='student':
        courses=course.objects.all()
        return render(request,'project/CoursesList.html',{'courses':courses})
    courses()

@login_required
def addcourse(request):
    if request.user.typeof=='teacher':
        if (request.method == 'GET'):
            return render(request,'project/AddCourse.html',{'form':courseForm()})
        else:
         form=courseForm(request.POST)
         new_course=form.save(commit=False)
         new_course.id_teacher=request.user
         new_course.save()
         return redirect('courses') 
    else:
        return redirect('courses') 
@login_required
def updatecourse(request,course_pk):
    if request.user.typeof=='teacher':
       ucourse=get_object_or_404(course,pk=course_pk,id_teacher=request.user)
       if request.method == 'GET':
              form=courseForm(instance=ucourse)
              return render(request,'project/UpdateCourse.html',{'course':ucourse,'form':form})
       else:
              
                   form=courseForm(request.POST,instance=ucourse)
                   form.save()
                   return redirect('courses')
    else:
             return redirect('courses') 

@login_required              
def deletecourse(request,course_pk):
    if request.user.typeof=='teacher':
        dcourse=get_object_or_404(course,pk=course_pk,id_teacher=request.user)
        dcourse.delete()
        return redirect('courses') 
    else:
        return redirect('courses') 

@login_required
def viewcourse(request,course_pk):
       vcourse=get_object_or_404(course,pk=course_pk)
       if request.method == 'GET':
            
           return render(request,'project/CoursesView.html',{'course':vcourse})
       else:
            
            return render(request,'project/CoursesView.html',{'course':vcourse})
    
