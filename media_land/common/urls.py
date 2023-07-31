from django.urls import path
from media_land.common import views

urlpatterns = [
    path('', views.index, name='home page'),
]
