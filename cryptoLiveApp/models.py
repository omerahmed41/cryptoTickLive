from django.db import models
import json


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExchangeRate(TimeStampMixin):
   exchangeRate = models.CharField(max_length=30)
   class Meta:
        ordering = ['id']

   def __str__(self):
        return self.exchangeRate
# Create your models here.