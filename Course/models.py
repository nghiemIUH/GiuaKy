from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
# Create your models here.
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='image')
