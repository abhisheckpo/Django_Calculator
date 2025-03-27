from django.db import models

class SumRecord(models.Model):
    num1 = models.IntegerField()
    num2 = models.IntegerField()
    sum_result = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
