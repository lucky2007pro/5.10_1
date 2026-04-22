from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from .models import User, Category, Product
from .serializers import UserSerializer, CategorySerializer, ProductSerializer


class UserListCreateView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(is_active=True) # (Agar is_active degan maydon bo'lsa)

    def perform_create(self, serializer):
        serializer.save()


class UserDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        instance = serializer.save()
        print(f"{instance.id} id'li foydalanuvchi yangilandi!")

    def perform_destroy(self, instance):
        print(f"{instance} o'chirib yuborilmoqda...")
        instance.delete()


from rest_framework.generics import ListAPIView, CreateAPIView

class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        search_query = self.request.query_params.get('search', None)
        if search_query:
            qs = qs.filter(name__icontains=search_query)
        return qs

class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save()