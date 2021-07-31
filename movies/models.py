from django.core.exceptions import ValidationError
from django.db import models
from django_mysql.models import ListCharField
from datetime import datetime
from django.db.models.signals import pre_save
from django.dispatch import receiver
# Create your models here.

def validate_popularity(value):
    '''Popularity of the movie should be between 0.0 and 100.0'''
    if value >=0 and value <=100:
        pass
    else:
        raise ValidationError("Popularity should be between 0.0 to 100.0")

def validate_imdb_score(value):
    '''IMDB score should be between 0.0 and 10.0'''
    if value >=0 and value <=10:
        pass
    else:
        raise ValidationError("Popularity should be between 0.0 to 10.0")



class Movies(models.Model):
    popularity99 = models.DecimalField(max_digits=4, decimal_places=1, validators=[validate_popularity])
    director = models.CharField(max_length=50)
    genre = ListCharField(base_field=models.CharField(max_length=15),size=10, max_length=(15*11))
    imdb_score = models.DecimalField(max_digits=3, decimal_places=1, validators=[validate_imdb_score])
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.name
    
    #Same directors can't have the same movie
    class Meta:
        unique_together = ['name', 'director']



#name of the director and movie name will be capitalized before being inserted to the database
@receiver(pre_save, sender=Movies)
def update_name(sender, instance, **kwargs):
    # temp_genre_list = []
    instance.name = instance.name.title()
    instance.director = instance.director.title()






    
