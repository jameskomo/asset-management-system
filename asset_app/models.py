from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Assets(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_serial_No = models.CharField(max_length=100)
    asset_location = models.CharField(max_length=100)
    asset_manufacturer = models.CharField(max_length=100)
    date_purchased = models.DateTimeField()
    asset_issued = models.BooleanField()
    date_issued = models.DateTimeField(default=timezone.now)
    asset_assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    asset_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assets-detail', kwargs={'pk': self.pk})



