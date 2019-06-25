from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from django.conf import settings
from django.core.files.storage import FileSystemStorage

import numpy as np
import cv2
import os
import time

from food_ai.utils import recognize, get_nutrisi

def api_check(request):
    data = {
        'status': 'ok',
        'method': request.method
    }
    return JsonResponse(data)

def get_berat(request):
    data = {
        'berat': 200,
        'berat1': 200
    }
    return JsonResponse(data)

def recognize_food(request):
    data = {
        'status': 'ok',
        'method': request.method
    }
    if request.method == 'POST' and request.FILES['img_data']:
        start_time = time.time()
        img_data = request.FILES['img_data']
        img_data1 = request.FILES['img_data1']
        cls_name, acc = recognize(img_data)
        cls_name1, acc1 = recognize(img_data1)

        nutrisi = get_nutrisi(cls_name)
        nutrisi1 = get_nutrisi(cls_name1)

        cls_name = cls_name.replace('_',' ')
        cls_name = ' '.join(word[0].upper() + word[1:] for word in cls_name.split())

        cls_name1 = cls_name1.replace('_',' ')
        cls_name1= ' '.join(word[0].upper() + word[1:] for word in cls_name1.split())

        data['cls_name'] = cls_name
        data['acc'] = acc
        data['cls_name1'] = cls_name1
        data['acc1'] = acc1
        data['time'] = "%.2f" % (time.time() - start_time)
        data['nutrisi'] = nutrisi
        data['nutrisi1'] = nutrisi1

        return JsonResponse(data)
    
    return JsonResponse(data)


