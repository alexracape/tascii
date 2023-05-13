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
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_post_created')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='open') # open, accepted, completed, cancelled
    filled_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)s_post_filled', null=True, blank=True)

class Rating(models.Model):
    RATING_CHOICES = (
        (1, '1 Star'),
        (2, '2 Stars'),
        (3, '3 Stars'),
        (4, '4 Stars'),
        (5, '5 Stars'),
    )
    
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        unique_together = ('post', 'user')