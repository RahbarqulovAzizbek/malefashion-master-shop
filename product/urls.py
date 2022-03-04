from django.urls import path
from .views import update_wishlist, WishListView

app_name = 'products'

urlpatterns = [
    path('wishlist/', WishListView.as_view(), name='wishlist'),
    path('<int:pk>/wishlist/', update_wishlist, name='add_wishlist')
]