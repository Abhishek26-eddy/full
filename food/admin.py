from django.contrib import admin

# Register your models here.
from .models import Skills, Profile

admin.site.register(Skills)
admin.site.register(Profile)