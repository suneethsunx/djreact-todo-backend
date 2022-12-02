from django.urls import path
from .import views

urlpatterns = [
    path('notes/', views.getNotes, name='notes'),
    path('notes/<int:id>/', views.getNote, name='note'),
    path('notes/new/', views.newNote, name='new-note'),
    path('notes/delete/<int:id>/', views.deleteNote, name='delete-todo'),
    path('notes/update/<int:id>/', views.updateNote, name='update-note'),
]