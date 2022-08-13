from django.db import models

# Create your models here.
class CloudUser(models.Model):  #model field 연습한다고 만들어놓은 Model
    user_id = models.CharField(null=True, max_length=32, unique=True, verbose_name='ID')
    user_pw = models.CharField(null=True, max_length=128, verbose_name='PW')
    user_name = models.CharField(null=True, max_length=16, verbose_name='NAME')
    user_email = models.EmailField(null=True, blank=True, max_length=128, unique=True, verbose_name='E-mail')
    user_birthdate = models.DateField(null=True, blank=True)

    def __str__(self):  #java의 toString과 같은 느낌
        return self.user_name
