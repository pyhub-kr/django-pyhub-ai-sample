from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:room_pk>/", views.language_tutor_chat),
    path("analyst/titanic/", views.titanic_data_analyst_chat, name="analyst-titanic"),
]
