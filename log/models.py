from django.db import models


# Create your models here.
class log(models.Model):
    id = models.AutoField("id", primary_key=True, unique=True)
    time = models.TextField(default='')
    ip = models.TextField(default='')
    url = models.TextField(default='')
    action = models.TextField(default='')


class full_log(models.Model):
    id = models.AutoField('id', primary_key=True, unique=True)
    log_id = models.ForeignKey(on_delete=models.CASCADE, to='log')
    content = models.TextField('content', default='')
