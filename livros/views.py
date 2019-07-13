from rest_framework import viewsets, status, request
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Livro, Perfil, Compra
from .serializers import LivroSerializer, PerfilSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer
    permission_classes = [IsAuthenticated]


class LivroViewSet(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Livro.objects.exclude(perfil = self.request.user.perfil)

    def create(self, request):
        request.data["perfil"] = request.user.perfil.id
        livro_serializer = LivroSerializer(data=request.data)
        if livro_serializer.is_valid():
            livro_serializer.save()
            retorno = super(LivroViewSet, self).update(request)
            return retorno
        else:
            return Response(data={'erros': livro_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    def create(self, request):
        request.data["perfil"] = request.user.perfil.id
        livro_serializer = LivroSerializer(data=request.data)
        if livro_serializer.is_valid():
            livro_serializer.save()
            retorno = super(LivroViewSet, self).update(request)
            return retorno
        else:
            return Response(data={'erros': livro_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def comprar(self, request):
        try:
            livro  =  Livro.objects.get(pk=request.data["livro_id"])
            perfil =  request.user.perfil
            compra = Compra(perfil=perfil, livro=livro)
            compra.save()
        except ValueError:
            return Response(
                data={"errors": "Não foi possível fazer a compra"},
                status=status.HTTP_204_NO_CONTENT)
        return Response(data=["Compra realizada com sucesso"], status=status.HTTP_200_OK)

class MinhasCompras(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Livro.objects.filter(compra__perfil = self.request.user.perfil)

class MeusLivros(viewsets.ModelViewSet):
    serializer_class = LivroSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Livro.objects.filter(perfil = self.request.user.perfil)
