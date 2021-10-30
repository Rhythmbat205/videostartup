from django.db import models
from video_app.models import Post

# Create your models here.
class Booking(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='bookings')
    name = models.TextField()
    email = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    meeting_time = models.TextField()
    meeting_date = models.TextField()
    remarks = models.TextField()
