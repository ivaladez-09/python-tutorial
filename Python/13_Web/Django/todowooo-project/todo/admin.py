from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    """This is for being able to see the 'created' field from Todos model"""
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
