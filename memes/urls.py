from django.contrib import admin
from django.urls import path, include
from .views import CreateMemeView, MemeDeleteView, MemeDetailView, MemeLikeView
from mysite.views import MemeListView

app_name = "memes"

urlpatterns = [
    path('meme/create/', CreateMemeView.as_view(), name='add'),
    path('all/', MemeListView.as_view(), name='all'),
    path('meme/delete/<int:pk>/', MemeDeleteView.as_view(), name='delete'),
    path('meme/detail/<int:pk>/', MemeDetailView.as_view(), name='detail'),
    path('meme/like/<int:pk>', MemeLikeView, name='like'),

]
