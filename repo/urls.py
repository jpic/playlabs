from . import views
from django.views import generic
from repo.models import Repo
from django.urls import path, include

urlpatterns = [
    path('', views.RepoListView.as_view(), name='repo-list'),
    path('<pk>', generic.DetailView.as_view(model=Repo), name='repo-detail'),
    path('add/', views.RepoCreateView.as_view(), name='repo-create') 
]

