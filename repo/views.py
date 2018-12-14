from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import views
from .models import Repo
from django.http import HttpResponse
from django.views import generic
from django import forms
from shlex import quote
import os

#def index(request):
#    return HttpResponse("Hello, from repouser")


def index(request):
    return render(request,'repo/index.html')



class RepoForm(forms.ModelForm):
    conditions = forms.BooleanField(
        label='Accepter les CGV',
        required=True,
    )

    class Meta:
        model = Repo
        fields = [
            'repo_name',
            'src',
            'org',
            'conditions',
        ]


class RepoCreateView(generic.CreateView):
    model = Repo
    form_class = RepoForm

    def form_valid(self, form):
        form.instance.owner=self.request.user.username
        response = super().form_valid(form)
        os.system(f'bash /app/migrate.sh {self.request.user.id} {quote(form.instance.src)} {quote(form.instance.repo_name)} | tee /tmp/script.log ')

        return response


class RepoListView(generic.ListView):
    model = Repo
    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user.username)

