from django.urls import path
from .views import HomeTemplateView, AboutTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view()),
    # path('about-me', AboutTemplateView.as_view()),
]