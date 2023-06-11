from .models import Fmodel
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea
from django.contrib.auth.models import User

class FmodelForm(ModelForm):
    class Meta:
        model = Fmodel
        fields = ['title', 'annotation', 'full_text', 'date_write']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название новости'
            }),
            'annotation': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание новости'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Основное содержание новости'
            }),
            'date_write': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата публикации'
            }),
        }
