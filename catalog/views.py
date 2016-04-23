from django.shortcuts import render
from catalog.models import *
from django.http import HttpResponse,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import render_to_string
from django.core.context_processors import  csrf
from django.views.decorators.csrf import csrf_exempt
from datetime import *
import random
import string

# Create your views here.
def home(request):
    tovars = []
    for x in range(0,3):
        tovars.append(x)
    context = {
        'title': 'Helloworld',
        'tovars': tovars,
    }
    return HttpResponse(render_to_string('index.html', context=))