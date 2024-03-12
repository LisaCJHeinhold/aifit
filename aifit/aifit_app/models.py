from django.db import models

# Create your models here.

#Workout model -alyssa
class Workout(models.Model):
    type = models.CharField(max_length=100)
    date_created = models.DateField()
    time = models.IntegerField()
    number_exercises = models.IntegerField()

#exercise model -alyssa
class Exercise(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    reps = models.IntegerField()
    weight = models.IntegerField()
    sets = models.IntegerField()    
    description = models.CharField(max_length=100)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)


