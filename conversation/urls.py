from django.urls import path

from dashboard.urls import app_name
from . import views

app_name = 'conversation'

urlpatterns = [
    path('new/<int:item_pk>/', views.new_conversation, name='new')
]