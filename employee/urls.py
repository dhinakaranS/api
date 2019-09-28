from django.urls import path
from .views import emp

urlpatterns = [
    path('', emp)
]
