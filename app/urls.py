from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('design/', views.design, name='design'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
