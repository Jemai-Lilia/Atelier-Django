from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError

def validate_cin(value):
    if len(str(value)) !=8 :
        raise ValidationError("le cin doit contenir 8 chiffres")

def validate_email(value):
    if not str(value).endswith("@esprit.tn"):
        raise ValidationError("l'email doit se terminer par @esprit.tn")

# Create your models here.
class Person(AbstractUser):
    cin = models.CharField(
        primary_key=True,
        max_length=8,
        validators=[validate_cin]
    )
    email=models.EmailField(
        unique=True,
        validators=[validate_email]
    )