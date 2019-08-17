from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage
#yang ditambah
from . import utils

def makanan(request):
    return render(request,'home.html')

#ambek dari alzheimerai dan ubah disini
def hasil_json(request):

    data = {
        'name': request.POST.get('name', ''),
        'age': request.POST.get('age', ''),
        'height': request.POST.get('height', ''),
        'weight': request.POST.get('weight', ''),
        'gender': request.POST.get('gender', ''),
        'activity': request.POST.get('activity', ''),
    }
    utils.gerate_report(data)

    return JsonResponse(data)
