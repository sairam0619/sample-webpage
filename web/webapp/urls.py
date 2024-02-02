# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('submission-success/', views.submission_success, name='submission_success'),
]
