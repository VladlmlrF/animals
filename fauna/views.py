from django.shortcuts import render
from django.views.generic import ListView

from .models import Animal


class AnimalHome(ListView):
    model = Animal
    template_name = 'fauna/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        context['title'] = 'Главная страница'
        # context['cat_selected'] = 0
        return context

