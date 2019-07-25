from django.urls import path
from . import views

app_name='divaDoc'
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),

    #path(''),

    path('blogs/', views.blogs_view, name='blogs'),
#    path('medicines/', views.medicines_view, name='medicines'),

    #### Home
    path('userhome/', views.userhome, name='userhome'),

    #### Appointment
    path('appointment/', views.index_appointment, name='index_appointment'),
    path('appointment/<int:doc_id>', views.detail_appointment, name='detail_appointment'),
    path('appointment/<int:doc_id>/status/', views.status_appointment, name='status_appointment'),
    path('appointment/<int:doc_id>/book/', views.book_appointment, name='book_appointment'),
    path('appointment/<int:doc_id>/cancel/', views.cancel_appointment, name='cancel_appointment'),

    #### Rate
    path('feedback/', views.index_rate, name='feedback'),

    ## discussion forum
    path('discussion_forum/', views.discussion_forum, name='discussion_forum'),

    ## diva_opinion
    path('diva_opinion/', views.diva_opinion, name='diva_opinion'),

    path('user_logout/',views.user_logout, name='user_logout'),
]
