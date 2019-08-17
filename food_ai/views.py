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
        img_data2 = request.FILES['img_data2']
        img_data3 = request.FILES['img_data3']

        cls_name, acc = recognize(img_data)
        cls_name1, acc1 = recognize(img_data1)
        cls_name2, acc2 = recognize(img_data2)
        cls_name3, acc3 = recognize(img_data3)

        nutrisi = get_nutrisi(cls_name)
        nutrisi1 = get_nutrisi(cls_name1)
        nutrisi2 = get_nutrisi(cls_name2)
        nutrisi3 = get_nutrisi(cls_name3)

        cls_name = cls_name.replace('_',' ')
        cls_name = ' '.join(word[0].upper() + word[1:] for word in cls_name.split())

        cls_name1 = cls_name1.replace('_',' ')
        cls_name1= ' '.join(word[0].upper() + word[1:] for word in cls_name1.split())

        cls_name2 = cls_name2.replace('_',' ')
        cls_name2 = ' '.join(word[0].upper() + word[1:] for word in cls_name2.split())

        cls_name3 = cls_name3.replace('_',' ')
        cls_name3= ' '.join(word[0].upper() + word[1:] for word in cls_name3.split())

        data['cls_name'] = cls_name
        data['cls_name1'] = cls_name1
        data['cls_name2'] = cls_name2
        data['cls_name3'] = cls_name3

        data['acc'] = acc
        data['acc1'] = acc1
        data['acc2'] = acc2
        data['acc3'] = acc3

        data['time'] = "%.2f" % (time.time() - start_time)
        data['nutrisi'] = nutrisi
        data['nutrisi1'] = nutrisi1
        data['nutrisi2'] = nutrisi2
        data['nutrisi3'] = nutrisi3

        return JsonResponse(data)
    
    return JsonResponse(data)


