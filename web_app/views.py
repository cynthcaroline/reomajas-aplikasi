from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils.html import strip_tags
from docxtpl import DocxTemplate
from io import BytesIO

def generate_report(data : dict):
    template = DocxTemplate("media/template/template.docx")
    result_path = 'media/result/reomajas-report.docx'
    context = data
    template.render(context)
    template.save(result_path)
    
    return template

def makanan(request):
    return render(request,'home.html')

def report(request):
    konsumsi = strip_tags(request.POST.get('konsumsi', ''))

    data = {
        'name': request.POST.get('name', ''),
        'age': request.POST.get('age', ''),
        'height': request.POST.get('height', ''),
        'weight': request.POST.get('weight', ''),
        'gender': request.POST.get('gender', ''),
        'activity': request.POST.get('activity', ''),
        'kalori': request.POST.get('kalori', ''),
        'konsumsi': konsumsi
    }
    document = generate_report(data)
    data = {
        'status': 'ok',
        'method': request.method
    }
    return JsonResponse(data)