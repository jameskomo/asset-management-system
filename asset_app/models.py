from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})

class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=100)
    neighborhood_location = models.CharField(max_length=100)
    occupants_count = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood_image = models.ImageField(default="default.jpeg", upload_to = 'images/')
    

    def __str__(self):
        return self.neighborhood_name

    def get_absolute_url(self):
        return reverse('neighborhood-detail', kwargs={'pk': self.pk})

class Business(models.Model):
    business_name = models.CharField(max_length=100)
    business_location = models.CharField(max_length=100)
    business_email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True, blank=True)
    business_description=models.TextField()
    business_image = models.ImageField(default="default.jpeg", upload_to = 'images/')

    def __str__(self):
        return self.business_name

    def get_absolute_url(self):
        return reverse('business-detail', kwargs={'pk': self.pk})

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_number=models.TextField()
    contact_address = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    contact_logo = models.ImageField(default="default.jpeg", upload_to = 'media/images/')
    

    def __str__(self):
        return self.contact_name

    def get_absolute_url(self):
        return reverse('contact-detail', kwargs={'pk': self.pk})
