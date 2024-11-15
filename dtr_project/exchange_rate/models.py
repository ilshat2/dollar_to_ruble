from django.db import models

class ExchangeRate(models.Model):
    date = models.DateField(auto_now_add=True)
    decim = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Kурс на {self.date}: {self.decim}'
