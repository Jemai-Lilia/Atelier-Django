from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from person.models import Person
from django.utils import timezone

def validate_eventdate(value):
    if value< date.today():
        raise ValidationError("la date de l'event doit être supérieure à date actuelle")

# Create your models here.
class Event(models.Model):
    category_choices =[
        ("Musique","Musique"),
        ("Cinema","Cinéma"),
        ("Sport","Sport"),
    ]

    id=models.AutoField(primary_key=True)
    title= models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to="event/")
    category=models.CharField(max_length=30,choices=category_choices)
    state=models.BooleanField(default=False)
    nbr_participant=models.PositiveIntegerField(default=0)
    evt_date=models.DateField(validators=[validate_eventdate])
    creation_date=models.DateTimeField(auto_now_add=True)
    update_date=models.DateTimeField(auto_now=True)
    organizer=models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name="organizer"
    )
    class Meta:
        constraints=[
            models.CheckConstraint(
                check=models.Q(evt_date=timezone.now().date()),
                name="futur event date"
            )
        ]
    
class Participation(models.Model):
    person=models.ForeignKey(Person, on_delete=models.CASCADE)
    event=models.ForeignKey(Event,on_delete=models.CASCADE)
    participation_date=models.DateField(default=timezone.now)
    class Meta:
        unique_together=("person","event")