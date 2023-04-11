from django.db import models
from datetime import datetime, timedelta
    
class Person(models.Model):
    date_missing = models.DateField(default=datetime.today, blank=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    age_at_missing = models.IntegerField(default=0)  
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    race = models.CharField(max_length=50)

    def __str__(self):
        return (self.first_name)