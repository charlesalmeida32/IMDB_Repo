from django.core.exceptions import ValidationError
from django.db import models
from django_mysql.models import ListCharField
from datetime import datetime
# Create your models here.

def validate_popularity(value):
    if value >=0 and value <=100:
        pass
    else:
        raise ValidationError("Popularity should be between 0.0 to 100.0")

def validate_imdb_score(value):
    if value >=0 and value <=10:
        pass
    else:
        raise ValidationError("Popularity should be between 0.0 to 10.0")


class Movies(models.Model):
    popularity99 = models.DecimalField(max_digits=4, decimal_places=1, validators=[validate_popularity])
    director = models.CharField(max_length=50)
    # genre = ListCharField(base_field=models.CharField(max_length=15),size=10, max_length=(15*11))
    genre = ListCharField(base_field=models.CharField(max_length=15),size=10, max_length=(15*11))
    imdb_score = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return self.name
    

    class Meta:
        unique_together = ['name', 'director']




