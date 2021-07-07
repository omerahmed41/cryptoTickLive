from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('api/v1/quotes/', views.QuotesView.as_view(), name='quotes'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]