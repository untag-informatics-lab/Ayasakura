from django.db import models

class laboratories(models.Model):
    class Meta:
        db_table = "lab_laboratories"
    
    id          = models.AutoField(null=False)
    name        = models.CharField(null=False, max_length=40)
    picture     = models.CharField(null=False, max_length=255)
    location    = models.CharField(null=False, max_length=100)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
