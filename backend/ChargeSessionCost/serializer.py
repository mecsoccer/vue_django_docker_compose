from rest_framework import serializers
from .models import ChargeSessionCost

class ChargeSessionCostSerializer(serializers.ModelSerializer):

    class Meta:
        model = ChargeSessionCost 
        fields = ['id', 'user_info', 'location', 'energy_kWh', 'cost', 'charge_datetime']
