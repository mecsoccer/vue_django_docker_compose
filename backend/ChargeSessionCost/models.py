from django.db import models
from UserInfo.models import UserInfo 

class ChargeSessionCost(models.Model):
    user_info = models.ForeignKey(UserInfo, on_delete = models.CASCADE)
    location = models.CharField("Name", max_length=12)
    energy_kWh = models.FloatField()
    cost = models.FloatField()
    charge_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name