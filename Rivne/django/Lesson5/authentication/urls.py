from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signin/', views.sign_in, name='signin')
]
