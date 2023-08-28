from django.db import models


# Create your models here.
class Level(models.Model):
    id = models.AutoField(primary_key=True)
    level = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)
    connection = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'levels'
