from django.urls import include, path
from .views import RegisterView, Getuser

urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('users/<int:pk>/', Getuser.as_view(), name="get_user"),
]