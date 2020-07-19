from django.db import models
from django.conf import settings
# Create your models here.
class course(models.Model):
    CourseName=models.CharField(max_length=50)
    urlcourse=models.URLField() 
    about=models.TextField()
    id_teacher=models.ForeignKey(settings.AUTH_USER_MODEL,
        null=True, blank=True, on_delete=models.SET_NULL)
    
    

    
