from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
#from .forms import DocAuthenticationForm
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Doctor

# Create your views here.
class DoctorCreate(CreateView):
    model = Doctor
    fields = ['name', 'username', 'password', 'certficate', 'profile', 'location', 'available_dates', 'works_from','works_upto', 'curr_status', 'max_status']

def home_doc(request):
    return render(request, 'Doctor/home_doc.html', {})

def signup_doc(request):
    if request.method=='GET':
        q = Testdoc.objects.filter(name__startswith=request.GET['profile'])
        # q = Testdoc.objects.filter(id=1)
        c = q.choice_set.create(name=request.GET['username'], location=request.GET['location'], available_dates=request.GET['available_dates'], works_from=request.GET['works_from'], works_upto=request.GET['works_upto'], curr_status=request.GET['curr_status'], max_booking=request.GET['max_status'])
        c.save()
    return render(request, 'Doctor/doctor_form.html', {})

def login_doc(request):
    if request.method=='POST':
        print (request.POST)
        username = request.POST["username"]
        password = request.POST["password"]
        flag = 0
        for doc in Doctor.objects.all():
            if doc.username==username and doc.password==password and doc.validity==True:
                flag = 1
                break
        if flag==1:
            doc.active = True
            return render(request, 'Doctor/home_doc.html', {'doc':doc})
            #return redirect('Doctor:home_doc')
        else:
            return redirect('Doctor:login_doc')
    else:
        form = AuthenticationForm()
    return render(request, 'Doctor/login_doc.html', {'form':form})

def write_a_blog(request):
    return render(request, 'Doctor/write_a_blog.html', {})

def live_status(request):
    return render(request, 'Doctor/live_status.html', {})

def rating_doc(request):
    return render(request, 'Doctor/rating_doc.html', {})
