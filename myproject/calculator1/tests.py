from django.test import TestCase, Client
from django.urls import reverse
from .models import SumRecord
import json

class SumRecordTestCase(TestCase):
    def setUp(self):
        self.record = SumRecord.objects.create(num1=5, num2=7, sum_result=12)

    def test_sum_record_creation(self):
        """Test if SumRecord model saves correctly."""
        record = SumRecord.objects.get(id=self.record.id)
        self.assertEqual(record.num1, 5)
        self.assertEqual(record.num2, 7)
        self.assertEqual(record.sum_result, 12)

class CalculateSumAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse("calculate_sum")  # Gets the URL for `/api/sum/`

    def test_valid_sum_post_request(self):
        """Test API response with valid numbers."""
        response = self.client.post(
            self.url, 
            data=json.dumps({"num1": 10, "num2": 15}), 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sum": 25})

        # Check if the sum is stored in the database
        self.assertTrue(SumRecord.objects.filter(num1=10, num2=15, sum_result=25).exists())

    def test_missing_fields(self):
        """Test API response with missing fields."""
        response = self.client.post(self.url, data=json.dumps({}), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"sum": 0})  # Since defaults are 0

    def test_invalid_data(self):
        """Test API response with invalid data (string input)."""
        response = self.client.post(
            self.url, 
            data=json.dumps({"num1": "abc", "num2": 10}), 
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)  # Should return error
        self.assertIn("error", response.json())  # Error message should be in response
