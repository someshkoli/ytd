# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pytube as pt
# Create your views here.
@csrf_exempt
def index(req):
    print(req)
    return render(req,'index.ejs')
    #HttpResponse("hello")

@csrf_exempt
def download(req):
    return JsonResponse({"id":"someshkoli"})
