from django.contrib import admin
from .models.autor import Autor
from .models.lector import Lector
from .models.libro import Libro
from .models.user import User

admin.site.register(Autor)
admin.site.register(Lector)
admin.site.register(Libro)
admin.site.register(User)