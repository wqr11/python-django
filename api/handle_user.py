from django.http import HttpRequest, HttpResponseBadRequest
from asgiref.sync import sync_to_async

async def handle_tg_user(request: HttpRequest, tg_id: int):
    if not tg_id:
        return HttpResponseBadRequest("tg_id is necessary")

    try:
        found_user = await User.objects.filter(tg_id=tg_id).afirst()

        if not found_user:
            new_user = User(tg_id=tg_id)

            await sync_to_async(new_user.save)()

            return ({ "success": True, "event_type": "USER_CREATED" })
    
        return ({ "success": True, "event_type": "USER_EXISTS" })

    except Exception as e:
        print(e)
        return ({ "success": False })