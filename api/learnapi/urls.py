from rest_framework.authtoken import views
from django.urls import path,include
from .views import *
urlpatterns = [
    path('', api),
    path('pu/<int:pk>',pu,name="pu"),
    path('api-token-auth/', views.obtain_auth_token),
    path('login', login)
]
