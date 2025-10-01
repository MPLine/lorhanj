from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class UserProfile(models.Model):
    profileImage = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg', blank="true")
    sexChoice = [('m','M'),('f','F')]
    username =models.ForeignKey(User,on_delete=models.CASCADE) 
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100,unique=True)
    Adresse= models.CharField(max_length=100,blank=True)
    phone= models.CharField(max_length=20,unique=True,blank=True)
    sex =models.CharField(choices=sexChoice,blank=True)
    domaine = models.CharField(max_length=100)

    def __str__(self):
        return super().__str__()