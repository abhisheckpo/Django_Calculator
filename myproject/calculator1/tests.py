from django.test import TestCase, Client
from django.urls import reverse
from calculator1.models import CalculationRecord  
import json

class CalculationRecordTestCase(TestCase):
    def setUp(self):
        self.record = CalculationRecord.objects.create(num1=5, num2=7, result=12, operation='+')

    def test_calculation_record_creation(self):
        """Test if CalculationRecord model saves correctly."""
        record = CalculationRecord.objects.get(id=self.record.id)
        self.assertEqual(record.num1, 5)
        self.assertEqual(record.num2, 7)
        self.assertEqual(record.result, 12)
        self.assertEqual(record.operation, '+')

class CalculatorAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("calculate")

    def test_addition(self):
        """Test addition operation."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 10, "num2": 15, "operation": "+"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 25.0})
        self.assertTrue(CalculationRecord.objects.filter(num1=10, num2=15, result=25.0, operation='+').exists())

    def test_subtraction(self):
        """Test subtraction operation."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 20, "num2": 5, "operation": "-"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 15.0})

    def test_multiplication(self):
        """Test multiplication operation."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 6, "num2": 4, "operation": "*"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 24.0})

    def test_division(self):
        """Test division operation."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 30, "num2": 5, "operation": "/"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 6.0})

    def test_zero_division_error(self):
        """Test division by zero error."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 10, "num2": 0, "operation": "/"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Division by zero is not allowed"})

    def test_invalid_operation(self):
        """Test API response with an invalid operation."""
        response = self.client.post(
            self.url,
            data=json.dumps({"num1": 10, "num2": 5, "operation": "%"}),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid operation"})

    def test_invalid_data(self):
        """Test API response with invalid data (string input)."""
        response = self.client.post(
            self.url, 
            data=json.dumps({"num1": "abc", "num2": 10, "operation": "+"}), 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

