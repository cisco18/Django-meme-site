from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CreateUserForm
from django.utils import timezone
from memes.models import Meme
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q


class MemeListView(ListView):
    model = Meme
    paginate_by = 10


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        search_value = self.request.GET.get("search", False)
        queryset = self.get_queryset()
        meme_likes_list = list()

        if search_value:
            memes = Q(title__icontains=search_value)
            objects = Meme.objects.filter(memes).select_related().distinct().order_by('-created_at')[:10]
            if len(objects)>0:
                context['meme_list'] = objects
                context['search'] = search_value
            else:
                context['meme_list'] = False
        else:
            objects = Meme.objects.all().order_by('-created_at')
            context['meme_list'] = objects

        for meme in queryset:
            like_data = dict()
            like_data['total_likes'] = meme.total_likes()
            like_data['liked'] = meme.likes.filter(id=self.request.user.id).exists()
            like_data['id'] = meme.id
            meme_likes_list.append(like_data)




        context['meme_likes'] = meme_likes_list


        return context


class MemeDetailView(DetailView):
    model = Meme
    template_name = "memes/meme_detail.html"


class CreateUserView(SuccessMessageMixin, CreateView):
    model = User
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    success_message = "account was created successfully"
    success_url = '/login'


class UserLoginView(LoginView):
    template_name = "registration/login.html"
    success_url = "home.html"


class UserLogoutView(LogoutView):
    next_page = "home.html"
