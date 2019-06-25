from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

def makanan(request):
    return render(request,'home.html')