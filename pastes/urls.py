
from django.urls import path
from . import views





urlpatterns = [
    path('list/paste/', views.ListPasteView.as_view()),
    path('create/paste/', views.CreatePasteView.as_view()),
    path('paste/<int:pk>/', views.PasteView.as_view()),
    
]
