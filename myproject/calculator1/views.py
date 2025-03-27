from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import SumRecord  

@csrf_exempt
def calculate_sum(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            num1 = int(data.get("num1", 0))
            num2 = int(data.get("num2", 0))
            result = num1 + num2
            
            # Save to MySQL
            SumRecord.objects.create(num1=num1, num2=num2, sum_result=result)
            
            #Response
            return JsonResponse({"sum": result})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid request"}, status=400)
