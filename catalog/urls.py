from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'/books/', views.books, name='books')
]
