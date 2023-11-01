
from django.urls import path
from . import views

app_name = 'challenges'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('<int:challenge_pk>/', views.detail, name='detail'),
]
