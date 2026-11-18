from django.urls import path
from .views import UserRegisterView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'user'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='/home/'), name='logout'),
]