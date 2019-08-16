from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['skills'] = Skill.objects.all()
        context['works'] = RecentWork.objects.all()
        context['moocs'] = MOOC.objects.all()
        return context

class AboutTemplateView(TemplateView):
    template_name = 'about.html'

    # # override get context date method
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  # first, call super get context data
    #     context['about'] = About.objects.first()
    #     return context