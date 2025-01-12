from django.urls import path,include
from . import views

urlpatterns = [
    path('lapd_entry/', views.lapd_entry, name='lapd_entry')
]