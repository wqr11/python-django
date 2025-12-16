from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from json import dumps
from .models import User

def auth_user(request: HttpRequest):
    request = 