from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import CalculationRecord  # Updated model name to be more general

@csrf_exempt
def calculate(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = float(data.get("num1", 0))
            num2 = float(data.get("num2", 0))
            operation = data.get("operation", "+")
            
            # Perform calculation
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    return JsonResponse({"error": "Division by zero is not allowed"}, status=400)
                result = num1 / num2
            else:
                return JsonResponse({"error": "Invalid operation"}, status=400)
            
            # Save to MySQL database
            CalculationRecord.objects.create(num1=num1, num2=num2, operation=operation, result=result)
            
            return JsonResponse({"result": result})
        
        except Exception as e:
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
