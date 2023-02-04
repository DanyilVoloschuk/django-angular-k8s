from django.urls import path
from . import views

urlpatterns = [
    path('', views.HeroListCreate.as_view()),
    path('<int:pk>/', views.HeroRetrieveUpdateDelete.as_view())
]
