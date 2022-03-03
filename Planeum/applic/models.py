from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Registration(models.Model):
    login_text = models.CharField('login', max_length=20)
    password_text = models.CharField('password', max_length= 200)
    name_text = models.CharField('name', max_length=200)
    surname_text = models.CharField('surname', max_length=200)
    email_text = models.CharField('email', max_length=200)
    date_reg = models.DateTimeField('date of registration')

class Login(models.Model):
    loggin = models.ForeignKey(Registration, on_delete=models.CASCADE)
    login_text = models.CharField('login', max_length=20)
    password_text = models.CharField('password', max_length= 200)

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Login.objects.create(user=instance)
    instance.profile.save()