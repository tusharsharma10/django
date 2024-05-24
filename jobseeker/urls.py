
from django.contrib import admin
from django.urls import path

from .views import JobseekerInboxView
urlpatterns = [
    path('count/distinct', JobseekerInboxView.as_view(), name='jobseekerInboxView'),
]
