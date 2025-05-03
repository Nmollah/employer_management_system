from django.urls import path
from .views import (
    SignupView,
    MyTokenObtainPairView,
    ProfileView,
    EmployerListCreateView,
    EmployerDetailView
)

urlpatterns = [
    path('auth/signup/', SignupView.as_view(), name='signup'),
    path('auth/login/', MyTokenObtainPairView.as_view(), name='login'),
    path('auth/profile/', ProfileView.as_view(), name='profile'),
    path('employers/', EmployerListCreateView.as_view(), name='employer-list'),
    path('employers/<int:id>/', EmployerDetailView.as_view(), name='employer-detail'),
]