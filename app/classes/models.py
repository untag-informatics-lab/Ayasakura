from django.db import models
from app.course.models import courses
from app.civilian.models import civilians
import time

class classes(models.Model):
    class Meta:
        db_table = "classes_classes"

    id                  = models.AutoField(null=False)
    course_id           = models.ForeignKey(courses, on_delete=models.PROTECT)
    name                = models.CharField(null=False, max_length=10)
    moderator           = models.ForeignKey(civilians, on_delete=models.PROTECT)
    year_academic       = models.CharField(null=False, max_length=4, default=time.strftime("%Y"))
    date_start          = models.DateField(null=False)
    date_finish         = models.DateField(null=False)
    submission_deadline = models.DateField(null=True)
    created_at          = models.DateTimeField(auto_now_add=True)
    updated_at          = models.DateTimeField(auto_now=True)
