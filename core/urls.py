from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('comentarios/<int:user_id>/', views.comentarios, name='comentarios'),
]
