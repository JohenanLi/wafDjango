from django.db import models


# Create your models here.
class rules(models.Model):
    id = models.AutoField('id', primary_key=True, unique=True)
    content = models.TextField('content', default='')
    description = models.TextField('description', default='')
    action = models.TextField('action', default='')
