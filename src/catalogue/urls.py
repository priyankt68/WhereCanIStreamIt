from django.urls import path

from . import views

app_name = 'catalogue'

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('search/', views.Search.as_view(), name='search'),
]
