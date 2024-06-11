from django.contrib import admin

# Register your models here.
from .models import DoListModel

@admin.register(DoListModel)

class Admin(admin.ModelAdmin):
    list_display=['Task','Task_status','created_at']