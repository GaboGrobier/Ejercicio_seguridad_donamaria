from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Comentario

# Personalizar el modelo User en el admin
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    ordering = ('username',)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'contenido', 'fecha_creacion')
    search_fields = ('usuario__username', 'contenido')
    list_filter = ('fecha_creacion',)

admin.site.register(Comentario, ComentarioAdmin)

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username',)
    search_fields = ('username',)

admin.site.register(Usuario, UsuarioAdmin)
