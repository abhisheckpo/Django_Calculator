from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CalculationRecord
from .serializers import CalculationRecordSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response


@csrf_exempt
def calculate(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = float(data.get("num1", 0))
            num2 = float(data.get("num2", 0))
            operation = data.get("operation", "+")

            # Create a temporary model instance
            temp_record = CalculationRecord(num1=num1, num2=num2, operation=operation)

            # Use the model method to perform the calculation
            result = temp_record.calculate_result()
            temp_record.result = result
            temp_record.save()

            return JsonResponse({"result": result})

        except ZeroDivisionError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except ValueError as e:
            return JsonResponse({"error": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"error": f"Unexpected error: {str(e)}"}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)


@api_view(['GET'])
def latest_record(request):
    try:
        latest = CalculationRecord.objects.latest('created_at')
        serializer = CalculationRecordSerializer(latest)
        return Response(serializer.data)
    except CalculationRecord.DoesNotExist:
        return Response({"error": "No records found"}, status=404)
