from django.urls import path, include
from . import views

urlpatterns = [
    path('', view = views.home ),
    path('play/<str:room_code>', view=views.game)
]
