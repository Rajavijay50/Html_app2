from django.urls import path
from app1.views import *
app_name='app2'

urlpatterns=[
    path('first_app/',first_app,name='first_app'),
    path('first_app1/',first_app1,name='first_app1'),
]