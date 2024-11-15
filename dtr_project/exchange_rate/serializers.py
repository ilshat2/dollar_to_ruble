from rest_framework import serializers
from exchange_rate.models import ExchangeRate

class ExchangeRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRate
        fields = ('date', 'decim')
