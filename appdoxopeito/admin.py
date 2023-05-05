from django.contrib import admin
from .models import Title
from .models import Person

admin.site.register(Title)
admin.site.register(Person)