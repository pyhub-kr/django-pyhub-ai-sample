from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render
from .models import LLMChatRoom


@staff_member_required
def language_tutor_chat(request, room_pk: int):
    llm_chat_room, __ = LLMChatRoom.objects.get_or_create(pk=room_pk)
    conversation_pk = llm_chat_room.conversation.pk
    ws_url = f"/ws/example/chat/{conversation_pk}/"
    return render(request, "pyhub_ai/chat_room_ws.html", {
        "ws_url": ws_url,
    })


def titanic_data_analyst_chat(request):
    return render(request, "pyhub_ai/chat_room_ws.html", {
        "ws_url": "/ws/example/analyst/titanic/",
    })
