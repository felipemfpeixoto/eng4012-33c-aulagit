from django.contrib import admin
from .models import Title
from .models import Person

admin.site.register(Title) # registra o modelo de dados Title para que ele possa ser gerenciado na interface de administração
admin.site.register(Person)# o mesmo para o modelo de dados Person