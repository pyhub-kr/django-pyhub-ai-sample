from django.urls import path
from .consumers import LanguageTutorChatConsumer, TitanicDataAnalystChatConsumer

websocket_urlpatterns = [
    path("ws/example/chat/language-tutor/", LanguageTutorChatConsumer.as_asgi()),
    path("ws/example/analyst/titanic/", TitanicDataAnalystChatConsumer.as_asgi()),
]
