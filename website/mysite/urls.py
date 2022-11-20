from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('button', views.button, name="button"),
    path('button/results', views.button_results, name="button_results"),
    path('showcase', views.showcase, name="showcase"),
    path('showcase/results', views.showcase_results, name="showcase_reslults"),
]