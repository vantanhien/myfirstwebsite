from django.db import models

class Blog(models.Model):
    title= models.CharField(max_length=100)
    pub_date= models.DateTimeField()
    body=models.TextField(max_length=10000)
    image_blog=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.title
    def summary(self):
        return self.body[:100]
    def pub_date_round(self):
        return self.pub_date.strftime('%b %e %Y')
