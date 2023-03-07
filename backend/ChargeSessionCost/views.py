from django.shortcuts import render
from .models import ChargeSessionCost
from rest_framework import generics
from .serializer import ChargeSessionCostSerializer
from rest_framework.permissions import IsAuthenticated


class ChargeSessionCostList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    # queryset = ChargeSessionCost.objects.filter()[:15]
    serializer_class = ChargeSessionCostSerializer
    permission_classes = [IsAuthenticated]
    model = ChargeSessionCost
    paginate_by = 1

    def get_queryset(self):
        user = self.request.GET.get('user_info')
        page = 1
        limit = 15
        if self.request.GET.get('page'):
            page = int(self.request.GET.get('page'))
        if self.request.GET.get('limit'):
            limit = int(self.request.GET.get('limit'))
        if user:
            object_list = self.model.objects.filter(user_info=user)[(page - 1) * limit : limit + (page - 1) * limit]
        else:
            object_list = []
        return object_list
