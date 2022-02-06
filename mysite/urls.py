from django.contrib import admin
from django.urls import path, include
from .views import CreateUserView, MemeListView, LoginView, LogoutView

app_name = 'site'
urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
