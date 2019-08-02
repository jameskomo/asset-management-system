from django.contrib import admin
from .models import Post, Business, Neighborhood, Contact

admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Business)
admin.site.register(Contact)