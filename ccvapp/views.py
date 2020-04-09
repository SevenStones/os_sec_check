from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http import JsonResponse
from ccvapp.munger import winrm_cmd_munger
import json
# from django.conf import settings
# Create your views here.

@login_required
def landing(request):

    context = {}
    html = render(request, 'admin/landing.html', context)
    return html

@login_required
def run_tests(request):

    x = winrm_cmd_munger()

    return JsonResponse(x)

def login(request):
    context = {}
    html = render(request, 'admin/login.html', context)
    return html

def logout_page(request):
    auth.logout(request)
    context = {}
    html = render(request, 'admin/logged_out.html', context)
    return html
