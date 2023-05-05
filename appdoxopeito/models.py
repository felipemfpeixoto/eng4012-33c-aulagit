from django.db import models
import datetime

class Title(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()
  due_date = models.DateField(default=datetime.date.today)
  done = models.BooleanField()

class Person(models.Model):
  title = models.CharField(max_length=50, default='Não preenchido')
  birth_date = models.DateField(default=datetime.date.today)
  due_date = models.DateField(default=datetime.date.today)
  sex = models.CharField(max_length=15, default='Não preenchido')
