from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.book_summary ,name='book_summary'),
    path('generate_response', views.generate_response ,name='generate_summary'),
]
