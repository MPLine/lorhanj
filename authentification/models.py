from django.db import models

class UserProfile(models.Model):
    profileImage = models.ImageField(upload_to='profile_images', default='default_profile_image.jpg', blank="true")
    sexChoice = [('m','M'),('f','F')]
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100,unique=True)
    Adresse= models.CharField(max_length=100,blank=True)
    phone= models.CharField(max_length=20,unique=True)
    sex =models.CharField(choices=sexChoice)
    domaine = models.CharField(max_length=100)
    userID = models.IntegerField

    def __str__(self):
        return super().__str__()