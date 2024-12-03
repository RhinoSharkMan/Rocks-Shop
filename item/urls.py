from django.urls import path

from rockShop.urls import urlpatterns
from . import views

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', views.detail, name='detail')
]