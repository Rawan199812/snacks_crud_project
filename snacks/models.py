from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.
class Snack(models.Model):
    title = models.TextField()
    purchaser = models.ForeignKey(get_user_model(),on_delete= models.CASCADE)
    description = models.TextField()

    def get_absolute_url(self):
        return reverse('snack_detail',args=[str(self.id)]) ## to redirect to the details page
    def __str__(self):
        return self.title

