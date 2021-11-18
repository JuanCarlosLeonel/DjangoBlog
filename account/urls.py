from django.urls import path
from .views import register


urlpatterns = [
    path('registrar/', register.as_view(), name='registrar')
]