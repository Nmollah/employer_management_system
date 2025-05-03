from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Employer
from .serializers import UserSerializer, EmployerSerializer, MyTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class EmployerListCreateView(generics.ListCreateAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class EmployerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = EmployerSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'

    def get_queryset(self):
        return Employer.objects.filter(user=self.request.user)