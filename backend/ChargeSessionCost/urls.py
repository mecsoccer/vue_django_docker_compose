from django.urls import include, path
from .views import ChargeSessionCostList


urlpatterns = [
    path('', ChargeSessionCostList.as_view()),
]