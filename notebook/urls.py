from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:note_id>/', views.open_note, name='open_note'),
]