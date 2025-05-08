from django.db import models

class CalculationRecord(models.Model):
    num1 = models.FloatField()  # Supports decimal values
    num2 = models.FloatField()
    operation = models.CharField(max_length=1)  # Stores "+", "-", "*", or "/"
    result = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for records

    def __str__(self):
        return f"{self.num1} {self.operation} {self.num2} = {self.result}"

    def perform_addition(self):
        return self.num1 + self.num2

    def perform_subtraction(self):
        return self.num1 - self.num2

    def perform_multiplication(self):
        return self.num1 * self.num2

    def perform_division(self):
        if self.num2 == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return self.num1 / self.num2

    def calculate_result(self):
        if self.operation == '+':
            return self.perform_addition()
        elif self.operation == '-':
            return self.perform_subtraction()
        elif self.operation == '*':
            return self.perform_multiplication()
        elif self.operation == '/':
            return self.perform_division()
        else:
            raise ValueError("Invalid operation")
