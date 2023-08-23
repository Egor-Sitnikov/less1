import re
from django import forms
from .models import Advertisements
from django.forms import ModelForm
from django.db import models


class AdvertisementForm(ModelForm):
    class Meta:
        model = Advertisements
        fields = ('title', 'description', 'price', 'auction', 'image')
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                   'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
                   'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                   'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title and re.match(r'^\?', title):
            raise forms.ValidationError('Заголовок не должен начинаться с вопросительного знака')
        return title


# class AdvertisementForm(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(
#         widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(
#         widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False,
#                                  widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     image = forms.ImageField(
#         widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'})
#     )