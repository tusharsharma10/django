from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . service import JobeekerService

from jobseeker.decorators import validateResId


# Create your views here.


class JobseekerInboxView(APIView):

    def get(self, request, *args, **kwargs):
        return JobeekerService.getCount(request)


