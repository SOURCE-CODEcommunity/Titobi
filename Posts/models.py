from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

#for featured items
class post(models.Model):

    title = models.CharField(max_length= 75)
    body = models.TextField()

    slug = models.SlugField()
    date = models.DateField(auto_now_add= True)
    banner= models.ImageField(default= 'image.png', blank= True)

    def __str__(self):
        return self.title

#for background image and home
class init_img(models.Model):

    title = models.CharField(max_length= 75)
    body = models.TextField()

    date  = models.DateField(auto_now_add= True)
    banner = models.ImageField(default= 'image.png', blank= True)

    def __str__(self):
        return self.title

#for item spinner in home
class gif(models.Model):

    title = models.CharField(max_length= 75)

    image = models.ImageField(default= 'image.png', blank= True,
            validators= [FileExtensionValidator(allowed_extensions= ['gif', 'jpg', 'jpeg', 'png'])])


    def __str__(self):
        return self.title

class detail(models.Model):
    title = models.CharField(max_length= 75)
    body = models.TextField()

    date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title

#for Placing order
class order(models.Model):

    title = models.CharField(max_length= 75)

    # image = models.ImageField(default= 'image.png', blank= True)

    phone_number = models.CharField(max_length= 20)

    contact_method = models.CharField(max_length= 50)

    date = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.title