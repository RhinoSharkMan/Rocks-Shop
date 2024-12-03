from  django.url import path

from . import views

urlpatterns = [
    path("", views.marketPlaceView, name='marketPlaceView')
]