from django.contrib import admin
from .models import Bug, Category, Tag

# Register your models here.
admin.site.register(Bug)
admin.site.register(Category)
admin.site.register(Tag)