from rest_framework import serializers
from .models import CalculationRecord

class CalculationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CalculationRecord
        fields = ['num1', 'num2', 'operation', 'result', 'created_at']
