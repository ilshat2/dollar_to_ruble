import requests
from django.http import JsonResponse
from exchange_rate.models import ExchangeRate
from exchange_rate.serializers import ExchangeRateSerializer


def get_current_usd(request):
    url = 'https://api.exchangeratesapi.io/latest'
    response = requests.get(url, params={'base': 'USD', 'symbols': 'RUB'})
    json = response.json()
    rate_now = json['rates']['RUB']

    ExchangeRate.objects.create(decim=rate_now)

    last_ten_rates = ExchangeRate.objects.order_by('-date')[:10]

    serializer = ExchangeRateSerializer(last_ten_rates, many=True)

    return JsonResponse({'rate_now': rate_now, 'history': serializer.data})
