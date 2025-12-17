from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, Http
from .models import User
from .handle_user import handle_tg_user

async def create_todo(request: HttpRequest, tg_id: int):
    if request.method != 'POST': return

    data = handle_tg_user(request, tg_id)

    content = request.POST.get("content")



