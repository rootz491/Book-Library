from django.urls import path
from . import views

app_name = 'catalog'

urlpatterns = [
    path(r'', views.IndexView.as_view(), name='index'),
    path(r'book/', views.BookListView.as_view(), name='books'),
    path(r'book/<int:pk>/', views.BookDetailView.as_view(), name='detail')
]
