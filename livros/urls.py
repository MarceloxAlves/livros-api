"""livros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


from .views import LivroViewSet, PerfilViewSet, MinhasCompras, MeusLivros

router = DefaultRouter()
router.register(r'livros', LivroViewSet, base_name="livros")
router.register(r'perfis', PerfilViewSet, base_name="perfis")
urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
    path('auth/login/', obtain_jwt_token),
    path('auth/refresh-token/', refresh_jwt_token),
    path('livros/comprar/', LivroViewSet.as_view({"post": "comprar"})),
    path('minhas-compras/', MinhasCompras.as_view({"get" : "list"})),
    path('meus-livros/', MeusLivros.as_view({"get" : "list"})),
]
