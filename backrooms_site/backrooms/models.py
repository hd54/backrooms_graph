from django.db import models


# Create your models here.
class Level(models.Model):
    level = models.CharField(unique=True)
    description = models.CharField()
    link = models.URLField(null=False, unique=True)
    connection = models.JSONField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'levels'
