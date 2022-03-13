from django.contrib import admin
from .models import Todo1

# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display =("title", "desp", "complited")

admin.site.register(Todo1, TodoAdmin)