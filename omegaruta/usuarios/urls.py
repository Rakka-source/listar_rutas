from django.urls import path
from .views import CustomLoginView, CustomLogoutView, vista_principal

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('', vista_principal, name='principal'),
]
