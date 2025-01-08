from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render


@staff_member_required
def language_tutor_chat(request):
    return render(request, "pyhub_ai/chat_room_ws.html", {
        "ws_url": "/ws/example/chat/language-tutor/",
    })


def titanic_data_analyst_chat(request):
    return render(request, "pyhub_ai/chat_room_ws.html", {
        "ws_url": "/ws/example/analyst/titanic/",
    })
