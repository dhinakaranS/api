from django.urls import path
from .views import emp, emp_details

urlpatterns = [
    path('', emp),
    path('employees/<int:pk>/', emp_details)
]
