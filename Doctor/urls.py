from django.urls import path
from . import views

app_name = 'Doctor'
urlpatterns = [
    path('', views.home_doc, name='home_doc'),
    path('signup/', views.DoctorCreate.as_view(), name='signup_doc'),
    path('login/', views.login_doc, name='login_doc'),
    path('write_a_blog/', views.write_a_blog, name='write_a_blog'),
    path('live_status/', views.live_status, name = 'live_status'),
    path('rating_doc/', views.rating_doc , name='rating_doc'),
]
