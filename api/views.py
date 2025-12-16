from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest
from json import dumps
from .models import User

async def auth_user(request: HttpRequest, tg_id: int):
    if not tg_id:
        return HttpResponseBadRequest("tg_id is necessary")

    try:
        found_user = await User.objects.filter(tg_id=tg_id).afirst()

        if not found_user:
            new_user = User(tg_id=tg_id)

            new_user.save()

            return JsonResponse({ "success": True, "event_type": "USER_CREATED" })
    
        return JsonResponse({ "success": True, "event_type": "USER_EXISTS", "data": data })

    except Exception as e:
        print(e)
        return JsonResponse({ "success": False })

