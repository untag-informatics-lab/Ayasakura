from django.db import models
from django.contrib.auth.models import User
from app.classes.models import classes


class civilians(models.Model):
    class Meta:
        db_table = 'civilian_civilians'

    role_choices    = ((1,'citizen'),(2,'council'),(3,'saint'))
    lab_choices     = ((1, 'komputasi'), (2, 'daskom'), (3, 'mikro'), (4, 'jarkom'), (5, 'citra'), (6, 'all'), (7, 'guest'))
    id              = models.AutoField(primary_key=True)
    id_user         = models.OneToOneField(User, on_delete=models.PROTECT)
    lab_id          = models.CharField()
    civilian_id     = models.IntegerField(null=False)
    name            = models.CharField(null=False, max_length=80)
    phone           = models.CharField(null=True, max_length=20)
    role_access     = models.CharField(choices=role_choices, null=False, max_length=10, default=1)
    lab_access      = models.CharField(choices=lab_choices, null=False, max_length=10, default=7)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)


class finalScore(models.Model):
    class Meta:
        db_table = "civilian_finalScore"

    id              = models.AutoField(null=False)
    civilians_id    = models.ForeignKey(civilians, on_delete=models.PROTECT)
    classes_id      = models.ForeignKey(classes, on_delete=models.PROTECT)
    final_score     = models.FloatField(null=False, max_length=5, default=0)
    final_grade     = models.CharField(null=False, max_length=3, default="E")
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)