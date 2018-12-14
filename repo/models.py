from django.db import models
from django.urls import reverse
from datetime import date as dtime
# Create your models here.

class Repo(models.Model):
    org = models.CharField("organisation",max_length=100, blank=True, null=True)
    repo_name = models.CharField("repo_name",max_length=30)
    src = models.URLField("repo_src",max_length=100,null=False, blank=False)
    owner = models.CharField("owner",max_length=100)
    date_crea = models.DateField("date", default=dtime.today)
    accept = models.BooleanField(default=True )
    #last_modif = models.DateField("Date", default=dtime.today)
    def __str__(self):
        return self.repo_name

    def get_absolute_url(self):
        return reverse('repo-detail', args=[self.pk])
