from django.db import models

# Create your models here.

class DoListModel(models.Model):
    Task=models.CharField(max_length=250)
    Task_status=models.BooleanField(default=False)
    created_at=models.TimeField(auto_now_add=True)