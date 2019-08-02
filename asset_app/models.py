from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


ASSET_CHOICES = (
    ("Desk", "Desk"),
    ("Laptop", "Laptop"),
    ("IP Phone", "IP Phone"),
    ("Project", "Project"),
)

LOCATION_CHOICES = (
    ("Ground Floor", "Ground Floor"),
    ("Mezzanine", "Mezzanine"),
    ("Second Floor", "Second Floor"),
    ("Meeting Room", "Meeting Room"),
)
class Assets(models.Model):
    asset_name = models.CharField(max_length=100, choices=ASSET_CHOICES)
    asset_serial_No = models.CharField(max_length=100)
    asset_manufacturer = models.CharField(max_length=100)
    date_purchased = models.DateTimeField()
    asset_issued = models.BooleanField(default=False)
    asset_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.asset_name

    def get_absolute_url(self):
        return reverse('assets-detail', kwargs={'pk': self.pk})


class AssetsIssuance(models.Model):
    asset=models.ForeignKey(Assets,on_delete=models.PROTECT)
    asset_location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    date_issued = models.DateTimeField(default=timezone.now)
    asset_assignee = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.asset

    def get_absolute_url(self):
        return reverse('assets-detail', kwargs={'pk': self.pk})
