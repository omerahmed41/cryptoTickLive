from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('', views.index.as_view(), name='index'),
    path('api/v1/quotes/', views.QuotesView.as_view(), name='quotes'),  #todo: add route group for 'api/v1'
    path('api/v1/startBackgroundTasks/', views.background, name='background'),  #todo: add route group for 'api/v1'
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]