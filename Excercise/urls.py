from django.urls import path
from . import views

app_name='Excercise'
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:dis_id>/', views.detail, name='detail'),
]
