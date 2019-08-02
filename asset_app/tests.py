from django.test import TestCase
import datetime as dt
from .models import Post, Neighborhood,Business,Contact

class NeighborhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.neighborhood= Neighborhood(neighborhood_name = 'Red Ville', neighborhood_location ='Liam Street', occupants_count ='100', neighborhood_image='media/images/default.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.neighborhood,Neighborhood))

class BusinessTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.business= Business(business_name = 'Komo Enterprises', business_location ='Liam Street', business_email ='test@testing.com', business_description='Dealing in all things household', business_image='media/images/default.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.business,Business))

class ContactTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.contact= Contact(contact_name = 'Kenya Health', contact_address='Liam Street', contact_email ='test@testing.com', contact_logo='media/images/default.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.contact,Contact))

class PostTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.assets= Post(title = 'First Post', content='This is my first posting', date_posted ='May 20, 2018', post_image='media/images/default.jpg')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.assets,Post))


      

    def tearDown(self):
        Neighborhood.objects.all().delete()
        Post.objects.all().delete()
        Business.objects.all().delete()
        Contact.objects.all().delete()
    
   