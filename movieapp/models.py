from django.db import models

class Movie(models.Model):
    name=models.CharField(max_length=50)
    dis=models.TextField()
    yr=models.IntegerField()
    img=models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name
    
