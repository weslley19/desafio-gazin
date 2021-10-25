from django.contrib import admin
from .models import Users


@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sexo', 'age', 'hobby', 'birthdate', 'created_at', 'updated_at', 'active')
    search_fields = ['name', 'sexo', 'age']
