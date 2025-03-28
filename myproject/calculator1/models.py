from django.db import models

class CalculationRecord(models.Model):
    num1 = models.FloatField()  # Supports decimal values
    num2 = models.FloatField()
    operation = models.CharField(max_length=1)  # Stores "+", "-", "*", or "/"
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for records

    def __str__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"
