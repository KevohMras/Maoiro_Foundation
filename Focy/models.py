from django.db import models

class MyModel(models.Model):
    Name = models.CharField(max_length=20)
    Phone_number = models.IntegerField()
    Email = models.CharField(max_length=20)
    Message = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'