from django import forms
from django.forms import ModelForm
from myapp.models import *

class ItensForm(forms.ModelForm):
    class Meta:

        model = Itens
        fields = "__all__"
        labels = {
            "name": "nome",
            "descript": "descrição",
            "path": "imagem",
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Nome do item",
                }
            ),
            'descript': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Escreva uma breve descrição",
                }
            ),
            'path': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Imagem",
                }
            ),
        }