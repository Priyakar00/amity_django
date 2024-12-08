from django.db import models

#model create table and fields in database
# Create your models here.
class student(models.Model):
	roll=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=100)
	course=models.CharField(max_length=100)
	marks=models.IntegerField()
