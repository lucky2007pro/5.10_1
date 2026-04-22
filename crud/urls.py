from django.urls import path

from .views import *

urlpatterns = [
    path('users/', UserListCreateView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
]