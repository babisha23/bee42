from django.urls import path
from . import views


urlpatterns=[
path('acDetails',views.ac_details,name='acDetails'),
path('regi',views.register,name='regi'),
path('out',views.logout,name='out')

]