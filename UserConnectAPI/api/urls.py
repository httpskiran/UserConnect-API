from django.urls import path
from .views import PublicAPIView, ProtectedAPIView

urlpatterns = [
    path('public/', PublicAPIView.as_view(), name='public'),
    path('protected/', ProtectedAPIView.as_view(), name='protected'),
]
