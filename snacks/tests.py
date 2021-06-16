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

    def test_snack_list_view(self):
        response = self.client.get(reverse("snack_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cake")
        self.assertTemplateUsed(response, "snack_list.html")

    def test_snack_detail_view(self):
        response = self.client.get(reverse("snack_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: ali")
        self.assertTemplateUsed(response, "snack_detail.html")

    def test_snack_create_view(self):
        response = self.client.post(
            reverse("snack_create"),
            {
                "title": "Krabby Patty",
                "purchaser": self.user.id,
                "description": "yum",
            }, follow=True
        )

        self.assertRedirects(response, reverse("snack_detail", args="2"))
        self.assertContains(response, "yum")

    def test_snack_update_view_redirect(self):
        response = self.client.post(
            reverse("snack_update", args="1"),
            {"title": "new title for Krabby Patty","description":"bad","purchaser":self.user.id}
        )
        self.assertRedirects(response, reverse("snack_detail", args="1"))

    def test_snack_delete_view(self):
        response = self.client.get(reverse("snack_delete", args="1"))
        self.assertEqual(response.status_code, 200)


