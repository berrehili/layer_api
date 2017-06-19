from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class UserInfos(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)
	firstname = models.CharField(max_length=10, null=True, blank=False,db_column='firstname')
	lastname = models.CharField(max_length=10, null=True, blank=False)
	email = models.EmailField()
	phone_regexp = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
	phone_number = models.CharField(validators=[phone_regexp], blank=False,max_length=15)
	birthday = models.DateField()


