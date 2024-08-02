
from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:note_id>/edit/', views.edit, name='edit'),
    path('<int:note_id>/delete/', views.delete, name='delete'),
    path('preview/', views.preview, name='preview'),
]
