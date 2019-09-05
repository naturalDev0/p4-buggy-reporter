from django.db import models
from web_accounts.models import MyUser

# Create your models here.

# Declare a class named "Bug"
class Bug(models.Model):
    name = models.CharField(max_length=30, blank=False)
    description = models.TextField(max_length=255, blank=True)
    done = models.BooleanField(blank=False, default=False)
    completed_at = models.DateField(blank=True, null=True, default=None)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
    
    def __str__(self):
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return self.name
        
class Tag(models.Model):
    name = models.CharField(max_length=50, blank=False)
    
    def __str__(self):
        return self.name