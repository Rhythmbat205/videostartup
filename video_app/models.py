from django.db import models
import uuid
from django.urls import reverse


# Create your models here.

def user_directory_path(instance, filename):
  
    # file will be uploaded to MEDIA_ROOT / user_<id>/<filename>
    return 'video_{0}'.format(filename)

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content =  models.FileField(upload_to = user_directory_path)
    title = models.TextField(max_length=50, verbose_name='title',default='title')
    category =models.TextField(max_length=50, verbose_name='category',default='category')
    
    def get_absolute_url(self):
        return reverse('postdetails', args=[str(self.id)])
        
    def __str__(self):
        return str(self.id)

