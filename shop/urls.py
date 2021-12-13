from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='hh'),
    path('<slug:c_slug>/<slug:product_slug>',views.pdtdetails,name='details'),
    path('serch',views.search,name='serch'),
]