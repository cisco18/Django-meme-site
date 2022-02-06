from django.views.generic import ListView, CreateView, DeleteView, DetailView, View
from memes.models import Meme
from .forms import CreateMemeForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils import timezone


@method_decorator(login_required, name='dispatch')
class CreateMemeView(CreateView):
    model = Meme
    form_class = CreateMemeForm
    template_name = 'memes/meme_form.html'
    success_message = "Congratulations you added a meme!"
    success_url = reverse_lazy('memes:all')

    def post(self, request, *args, **kwargs):
        form = CreateMemeForm(request.POST, request.FILES)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template_name, {'form': form})

            # Add owner to the model before saving
        meme = form.save(commit=False)
        meme.owner = self.request.user
        meme.save()
        return render(request, self.template_name, {'form': form})


@method_decorator(login_required, name='dispatch')
class MemeDeleteView(DeleteView):
    model = Meme
    fields = '__all__'
    success_url = reverse_lazy('memes:all')

    def get_queryset(self):
        print('delete get_queryset called')
        qs = super(MemeDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)


class MemeDetailView(DetailView):
    model = Meme
    template_name = "memes/meme_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        meme = get_object_or_404(Meme, id=self.kwargs['pk'])
        context['total_likes'] = meme.total_likes()
        context['owner'] = meme.owner.username

        liked = False
        if meme.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['liked'] = liked
        return context




def MemeLikeView(request, pk):
    meme = get_object_or_404(Meme, id=request.POST.get('meme_id'))
    liked = False
    if meme.likes.filter(id=request.user.id).exists():
        meme.likes.remove(request.user)
    else:
        meme.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('memes:all'))


def MemeLikeDetailView(request, pk):
    meme = get_object_or_404(Meme, id=request.POST.get('meme_id'))
    liked = False
    if meme.likes.filter(id=request.user.id).exists():
        meme.likes.remove(request.user)
    else:
        meme.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('memes:all'))
