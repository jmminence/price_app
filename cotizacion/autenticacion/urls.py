# en autenticacion/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView
from . import views

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('easy/', views.easy_view, name='easy'),
    path('arriservi/', views.arriservi_view, name='arriservi'),
    path('mct/', views.mct_view, name='mct'),
]