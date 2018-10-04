from django.contrib.auth.models import AbstractUser
from django.db import  models

class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)  #null is database related which means it can store an entry with no value, alternatively, blank is validation related.  If blank is true then a form will allow an empty value
    