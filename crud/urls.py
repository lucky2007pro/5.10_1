from django.urls import path
from .views import *
urlpatterns = [
    path('users/', UserView.as_view()),
    path('categories/', CategoryView.as_view()),
    path('products/', ProductView.as_view()),
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
    path('users/create/', UserCreateView.as_view()),
    path('categories/create/', CategoryCreateView.as_view()),
    path('products/create/', ProductCreateView.as_view()),
    path('users/<int:pk>/update/', UserUpdateView.as_view()),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view()),
    path('products/<int:pk>/update/', ProductUpdateView.as_view()),
    path('users/<int:pk>/delete/', UserDeleteView.as_view()),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view()),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view()),
    path('users/list/', UserListView.as_view()),
    path('categories/list/', CategoryListView.as_view()),
    path('products/list/', ProductListView.as_view()),
]