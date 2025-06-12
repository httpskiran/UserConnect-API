from django.urls import path
from .views import TriggerBotView

urlpatterns = [
    path('run-bot/', TriggerBotView.as_view(), name='run-bot'),
]
