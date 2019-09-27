from django.db import models
from app.course.models import courses
from app.civilian.models import civilians
from app.classes.models import classes

class task(models.Model):
    class Meta:
        db_table = "task_task"

    id          = models.AutoField(null=False)
    course_id   = models.ForeignKey(courses, on_delete=models.PROTECT)
    name        = models.CharField(null=False, max_length=75)
    description = models.TextField(null=False)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)


class submission(models.Model):
    class Meta:
        db_table = "task_submissions"
    
    id              = models.AutoField(null=False)
    task_id         = models.ForeignKey(task, on_delete=models.PROTECT)
    classes_id      = models.ForeignKey(classes, on_delete=models.PROTECT)
    civilian_id     = models.ForeignKey(civilians, on_delete=models.PROTECT)
    corrector_id    = models.ForeignKey(civilians, on_delete=models.PROTECT)
    filename        = models.CharField(null=False, max_length=255)
    is_plagarism    = models.BooleanField(null=False, default=False)
    score           = models.FloatField(null=False, default=0, max_length=5)
    review          = models.TextField(null=False, default="")


class presence(models.Model):
    class Meta:
        db_table = "task_presence"

    id              = models.AutoField(null=False)
    classes_id      = models.ForeignKey(classes, on_delete=models.PROTECT)
    civilian_id     = models.ForeignKey(civilians, on_delete=models.PROTECT)
    corrector_id    = models.ForeignKey(civilians, on_delete=models.PROTECT)
    score           = models.FloatField(null=False, default=70, max_length=5)
    review          = models.TextField(null=True, default="")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class exam(models.Model):
    class Meta:
        db_table = "task_exam"
    
    id              = models.AutoField(null=False)
    classes_id      = models.ForeignKey(classes, on_delete=models.PROTECT)
    civilian_id     = models.ForeignKey(civilians, on_delete=models.PROTECT)
    corrector_id    = models.ForeignKey(civilians, on_delete=models.PROTECT)
    score           = models.FloatField(null=False, default=70, max_length=5)
    review          = models.TextField(null=True, default="")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    