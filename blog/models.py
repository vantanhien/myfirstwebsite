from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=100)
    pub_date= models.DateTimeField()
    body=models.TextField(max_length=200)
    image_blog=models.ImageField(upload_to='image/')

