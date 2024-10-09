from django.db import models

# Create your models here.

class ProfileUser(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    birthdate = models.DateField()
    photo = models.ImageField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.user.username
