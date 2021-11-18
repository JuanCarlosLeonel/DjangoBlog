from django.urls import path
from .views import post_list, about, contact, post_create, post_update, post_delete, get_titles, post_detail

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<int:pk>/', post_detail.as_view(), name='post_detail'),
    path('criar/', post_create, name='post_create'),
    path('editar/<int:pk>/', post_update, name='post_update'),
    path('deletar/<int:pk>/', post_delete, name='post_delete'),
    path('sobre-nos/', about, name='about'),
    path('contato/', contact, name='contact'),  
    path('title/', get_titles, name='title'),
]