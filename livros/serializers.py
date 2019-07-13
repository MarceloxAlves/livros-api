from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Livro, Perfil


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Perfil
        fields = ('id', 'whatsapp', 'user')


class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Livro
        fields = ('id', 'titulo', 'autor', 'ano_escolar','valor','perfil')
