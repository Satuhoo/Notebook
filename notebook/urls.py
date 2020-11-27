from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:note_id>/', views.edit, name='edit'),
    path('create_note', views.create_note, name='create_note'),
    path('delete/<int:note_id>', views.delete, name='delete'),
]