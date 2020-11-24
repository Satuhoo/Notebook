from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('notebook/<int:note_id>/', views.open_note, name='open_note'),
    path('create_note', views.create_note, name='create_note'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]