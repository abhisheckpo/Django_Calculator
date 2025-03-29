from django.test import TestCase, Client
from django.urls import reverse
from .models import CalculationRecord
import json

class CalculationRecordTestCase(TestCase):
    def setUp(self):
        self.record = CalculationRecord.objects.create(num1=8, num2=2, operation="add", result=10)

    def test_record_saved_correctly(self):
        record = CalculationRecord.objects.get(id=self.record.id)
        self.assertEqual(record.num1, 8)
        self.assertEqual(record.num2, 2)
        self.assertEqual(record.operation, "add")
        self.assertEqual(record.result, 10)

class CalculatorAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("calculate")

    def test_addition(self):
        response = self.client.post(self.url, data=json.dumps({"num1": 6, "num2": 4, "operation": "add"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 10)

    def test_subtraction(self):
        response = self.client.post(self.url, data=json.dumps({"num1": 9, "num2": 3, "operation": "subtract"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 6)

    def test_multiplication(self):
        response = self.client.post(self.url, data=json.dumps({"num1": 5, "num2": 5, "operation": "multiply"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 25)

    def test_division(self):
        response = self.client.post(self.url, data=json.dumps({"num1": 10, "num2": 2, "operation": "divide"}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["result"], 5.0)

    def test_division_by_zero(self):
        response = self.client.post(self.url, data=json.dumps({"num1": 10, "num2": 0, "operation": "divide"}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_invalid_input(self):
        response = self.client.post(self.url, data=json.dumps({"num1": "abc", "num2": 10, "operation": "add"}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())

    def test_missing_fields(self):
        response = self.client.post(self.url, data=json.dumps({}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.json())
