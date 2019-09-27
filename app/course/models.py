from django.db import models
from app.lab.models import laboratories

class courses(models.Model):
    class Meta:
        db_table = "course_courses"
    
    id              = models.AutoField(null=False)
    laboratory_id   = models.ForeignKey(laboratories, on_delete=models.PROTECT)
    name            = models.CharField(null=False, max_length=100)
    description     = models.Charfield(null=False, max_length=255)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


