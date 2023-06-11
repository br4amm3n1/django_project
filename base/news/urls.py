from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create_news/', views.create_news, name='create'),
    path('<int:pk>/', views.NewsContents.as_view(), name='news_content'),
    path('mynews/<int:pk>/edit', views.NewsEdit.as_view(), name='news_edit'),
    path('mynews/<int:pk>/delete', views.NewsDelete.as_view(), name='news_delete'),
    path('mynews/', views.mynews_home, name='mynews_home')
]