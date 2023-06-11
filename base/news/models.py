from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Fmodel(models.Model):
    title = models.CharField('Название', max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    annotation = models.CharField('Описание', max_length=250)
    full_text = models.TextField('Статья')
    date_write = models.DateTimeField('Дата публикации')

    def get_absolute_url(self):
        return f'/news/{self.id}'

    def get_success_url(self):
        return f'/mynews/{self.id}'

    def __str__(self):
        return self.title
