from django.db import models
import datetime

# Aqui estão os dois modelos de entidades de cada lista
# Titles - títulos conquistados
#Person - pessoa importante para a história do clube

class Title(models.Model):
  title = models.CharField(max_length=50) # nome do título, Charfield recebe um conjunto de char
  #Precisa de um max_length, que guarda o tamanho do VARCHAR que será guardado no banco de dados
  description = models.TextField() # descrição do título, TextField pois será possível guardar textos maiores
  due_date = models.DateField(default=datetime.date.today) # Data atual, DateField pois irá guardar uma data
  done = models.BooleanField() # Feito, booleano para confirmar se acabou ou não

class Person(models.Model):
  title = models.CharField(max_length=50, default='Não preenchido') # nome da Pessoa, ex: Zico
  birth_date = models.DateField(default=datetime.date.today) # data de nascimento dessa pessoa
  due_date = models.DateField(default=datetime.date.today) # data atual
  sex = models.CharField(max_length=15, default='Não preenchido') # sexo dessa pessoa (Masculino / Feminino)
