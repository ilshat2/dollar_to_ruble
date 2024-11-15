import requests
from django.http import JsonResponse
from exchange_rate.models import ExchangeRate
from exchange_rate.serializers import ExchangeRateSerializer
#from dotenv import load_dotenv
import os


def get_current_usd(request):
    url = 'https://api.exchangeratesapi.io/v1/latest?access_key=api_key'
    api_key = os.getenv('API_KEY')
    response = requests.get(url, params={'base': 'EUR',
                                         'symbols': 'RUB',
                                         'access_key': api_key})
    
    if response.status_code == 200:
        json = response.json()
        rate_now = json.get('rates', {}).get('RUB', None)

        if rate_now is not None:
            ExchangeRate.objects.create(decim=rate_now)

            last_ten_rates = ExchangeRate.objects.order_by('-date')[:10]
            serializer = ExchangeRateSerializer(last_ten_rates,
                                                many=True)

            return JsonResponse({'Current exchange rate': rate_now,
                                 'Query history': serializer.data})
        else:
            return JsonResponse({'error': 'Bad Request'}, status=400)
    else:
        return JsonResponse({'error': '500'}, status=500)
