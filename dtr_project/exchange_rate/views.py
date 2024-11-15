import requests
from django.http import JsonResponse
from exchange_rate.models import ExchangeRate
from exchange_rate.serializers import ExchangeRateSerializer
import os


def get_current_usd(request):
    url = 'https://api.exchangeratesapi.io/v1/latest?access_key=api_key'
    api_key = os.getenv('API_KEY')
    response = requests.get(url, params={'base' : 'EUR',
                                         'symbols' : 'RUB',
                                         'access_key' : api_key})
    
    if response.status_code == 200:
        json = response.json()
        rate_now = json.get('rates', {}).get('RUB', None)

        if rate_now is not None:
            ExchangeRate.objects.create(decim=rate_now)

            last_ten_rates = ExchangeRate.objects.order_by('-date')[:10]
            serializer = ExchangeRateSerializer(
                last_ten_rates,
                many=True
            )
            
            query_histoty = [
                {"Дата запроса" : record["date"],
                "Курс рубля (RUB) к евро (EUR)" : record["decim"]}
                for record in serializer.data
            ]

            return JsonResponse(
                {'Текущий курс рубля (RUB) к евро (EUR)' : rate_now,
                'История запросов': query_histoty},
                json_dumps_params={'ensure_ascii' : False,
                                   'indent' : 4,}
            )
        else:
            return JsonResponse(
                {'error' : 'Bad Request'},
                status=400
            )
    else:
        return JsonResponse(
            {'error' : 'Internal Server Error'},
            status=500
        )
