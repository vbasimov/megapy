from rest_framework import serializers
from debtApp.models import Debt

class DebtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ('id', 'name', 'secondName', 'debtValue')