from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Snack


class SnacksTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="ali", 
            email = "ali@email.com",
            password="123456789"
        )
        self.snack = Snack.objects.create(
            title="Cake", description="nice" , purchaser=self.user
        )
    
    def test_string_representation(self):
        self.assertEqual(str(self.snack), "Cake")

    def test_snack_content(self):
        self.assertEqual(f"{self.snack.title}", "Cake")
        self.assertEqual(f"{self.snack.purchaser}", "ali")
        self.assertEqual(self.snack.description,"nice")

