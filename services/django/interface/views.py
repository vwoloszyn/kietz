from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
import pandas as pd
import glob
import os
import re
import random
from elasticsearch import Elasticsearch
from timeit import default_timer as timer
from datetime import timedelta
from collections import Counter
import math
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.mail import EmailMessage
from django.core.mail import send_mail, BadHeaderError
import urllib.request
#es = Elasticsearch([{'host':"es01",'port':"9200"}],http_auth=("elastic","nopassword"))
import json
import datetime
from django.shortcuts import redirect
import urllib.request
import json

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):


    return render(request,"index.html",{})



def login(request):
    #return render(request,"clean.html",{})
    return render(request,"login.html",{})



def search(request):

    return render(request,"clean.html",{})

