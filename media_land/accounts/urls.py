from django.urls import path, include
from media_land.accounts.views import RegisterUserView, LoginUserView, LogoutUserView, \
    ProfileDetailsView, EditProfileView, DeleteProfileView, shopping_cart

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register user'),
    path('login/', LoginUserView.as_view(), name='login user'),
    path('logout/', LogoutUserView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile details'),
        path('edit/', EditProfileView.as_view(), name='profile edit'),
        path('delete/', DeleteProfileView.as_view(), name='profile delete'),
    ])),
    path('shopping-cart/<int:pk>/', shopping_cart, name='shopping cart'),
]
