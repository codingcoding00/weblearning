from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Testdoc, TestChoice, rateapp
from django.urls import reverse

global k

def home(request):
    return render(request, 'divaDoc/home.html', {})

def signup_view(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('divaDoc:userhome')
    else:
        form = UserCreationForm()
    return render(request, 'divaDoc/signup.html', {'form': form})

def login_view(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            global k
            k = user
            login(request, user)
            return redirect('divaDoc:userhome')

    else:
        form = AuthenticationForm()
    return render(request, 'divaDoc/login.html', {'form': form})


"""
###### MEDICINES ####################################
def index_med(request):
    dis = disease.objects.order_by('id')
    return render(request, 'divaDoc/index_med.html', {'dis': dis})

def detail_med(request, dis_id):
    dise = get_object_or_404(disease, pk=dis_id)
    return render(request, 'divaDoc/detail_med.html', {'dise': dise})
"""

"""
def medicines_view(request):
    return render(request, 'divaDoc/medicines.html')
"""

def blogs_view(request):
    return render(request, 'divaDoc/blogs.html')


####logout
def user_logout(request):
    logout(request)
    form = AuthenticationForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'divaDoc/login.html', context)



############################  HOME  ##################

def userhome(request):
    return render(request, 'divaDoc/index_home.html',{'k':k})





##### Appointment ##################################

def index_appointment(request):
    doc = Testdoc.objects.order_by('id')
    return render(request, 'divaDoc/index_appointment.html', {'doc': doc})

def detail_appointment(request, doc_id):
    doctor = get_object_or_404(Testdoc, pk=doc_id)
    return render(request, 'divaDoc/detail_appointment.html', {'doctor': doctor})

def status_appointment(request, doc_id):
    doctor = get_object_or_404(Testdoc, pk=doc_id)
    return render(request, 'divaDoc/status_appointment.html', {'doctor': doctor})

def book_appointment(request, doc_id):
    doctor = get_object_or_404(Testdoc, pk=doc_id)
    try:
        selected_choice = doctor.choice_set.get(pk=request.POST['choice'])
    except(KeyError, TestChoice.DoesNotExist):
        context = {
            'doctor': doctor,
            'error_message': "You didn't select any doctor.",
        }
        return render(request, 'divaDoc/detail_appointment.html', context)
    else:
        if(selected_choice.curr_status < selected_choice.max_booking):
            selected_choice.curr_status += 1
            selected_choice.save()
        else:
            return HttpResponse('Sorry , appointment full for today !!')
        return HttpResponseRedirect(reverse('divaDoc:status_appointment', args=(doctor.id,)))

def cancel_appointment(request, doc_id):
    doctor = get_object_or_404(Testdoc, pk=doc_id)
    try:
        selected_choice = doctor.choice_set.get(pk=request.POST['choice'])
    except(KeyError, TestChoice.DoesNotExist):
        context = {
            'doctor': doctor,
            'error_message': "You didn't select any doctor.",
        }
        return render(request, 'divaDoc/detail_appointment.html', context)
    else:
        if(selected_choice.curr_status > 0):
            selected_choice.curr_status -= 1
            selected_choice.save()
        else:
            return HttpResponse("You didn't book this doctor !")
        return HttpResponseRedirect(reverse('divaDoc:status_appointment', args=(doctor.id,)))



############# RATE ##############

def index_rate(request):
    rat = rateapp.objects.order_by('id')
    return render(request, 'divaDoc/index_rate.html', {})


############  Diva Opinion ##########

def diva_opinion(request):
    return render(request, 'divaDoc/diva_opinion.html', {})

def discussion_forum(request):
    return render(request, 'divaDoc/discussion_forum.html', {})

"""
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                #return redirect('')
                return render(request, 'divaDoc/home.html', {})
            else:
                return render(request, 'divaDoc/login_form.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'divaDoc/login_form.html', {'error_message': 'Invalid login'})
    return render(request, 'divaDoc/login_form.html')


def signup(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Album.objects.filter(user=request.user)
                return redirect('/')
                #return render(request, 'divaDoc/home.html', {})
    context = {
        "form": form,
    }
    return render(request, 'divaDoc/signup_form.html', context)
"""
