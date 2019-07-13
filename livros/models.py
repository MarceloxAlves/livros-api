from django.contrib.auth.models import User
from django.db import models


class Perfil(models.Model):
    whatsapp =  models.CharField(max_length=20)
    user  =  models.OneToOneField(User, on_delete=models.CASCADE)

    @property
    def email(self):
        return self.user.email


class Livro(models.Model):
    titulo        =  models.CharField(max_length=200)
    autor         =  models.CharField(max_length=200)
    ano_escolar   =  models.CharField(max_length=4)
    valor         =  models.FloatField()
    perfil        =  models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="perfil")


class Compra (models.Model):
    perfil      =  models.ForeignKey(Perfil, on_delete=models.CASCADE)
    livro       =  models.ForeignKey(Livro, on_delete=models.CASCADE, related_name="compra")
    data_compra =  models.DateField(auto_now=True)
