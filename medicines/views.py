from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import disease, medicine
from django.urls import reverse

# Create your views here.

def index(request):
    dis = disease.objects.order_by('id')
    return render(request, 'medicines/index.html', {'dis': dis})

def detail(request, dis_id):
    dise = get_object_or_404(disease, pk=dis_id)
    return render(request, 'medicines/detail.html', {'dise': dise})
