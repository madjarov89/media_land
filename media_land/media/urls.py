from django.urls import path
from media_land.media import views

urlpatterns = [
    path('details/', views.media_details, name='media details'),
    path('add-media/', views.add_media, name='add media'),
    path('edit-media/', views.edit_media, name='add media'),
    path('delete-media/', views.delete_media, name='delete media'),
]
