from django.urls import path
from app_secu import views

urlpatterns = [
    path('',views.index,name='index')
]