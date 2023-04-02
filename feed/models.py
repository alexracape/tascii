from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    start_loc = models.CharField(max_length=100) # Could create custom location field to get long and lat too
    end_loc = models.CharField(max_length=100)
    expiration_date = models.DateTimeField()
    time_estimate = models.DurationField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)