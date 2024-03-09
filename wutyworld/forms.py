from django.forms import ModelForm
from .models import Juego


class JuegoForm(ModelForm):
    class Meta:
        model = Juego
        fields =[
                'titulo',
                'idioma',
                'edad',
                'principales',
                'secundarios',
        ]