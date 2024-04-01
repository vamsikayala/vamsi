from django.urls import path
from mobile.views import *
app_name='nothing'
urlpatterns=[
    path('oppo/',oppo,name='oppo')
]