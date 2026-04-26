from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.
class Diseases(models.Model):
    title=models.CharField(max_length=250,blank=False,null=False)
    Description=models.TextField(blank=False,null=False)
    image=models.ImageField(
        blank=True,
        null=True,
        upload_to='image/',
        validators=[FileExtensionValidator(['png','jpeg','jpg','webp','gif'])]
        )
    
    def __str__(self):
        return self.title
    
class Emergency(models.Model):
       title=models.CharField(max_length=250,blank=False,null=False)
       Description=models.TextField(blank=False,null=False)
       video=models.FileField(blank=True,null=True,upload_to='video/',
                               validators=[FileExtensionValidator(['mp4', 'mov', 'avi', 'mkv'])]
       )
       def __str__(self):
            return self.title