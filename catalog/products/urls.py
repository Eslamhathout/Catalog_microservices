from django.urls import path

from .views import ProductViewSet


urlpatterns = [
    path("product", ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),

    path("product/<int:pk>", ProductViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'delete',
    })),

]
