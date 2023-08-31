from django.db import models


# Create your models here.
class TEC_USER(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=100, null=True)


class TEC_USER_SESSION_WITH_HOSTNAME(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(TEC_USER, on_delete=models.CASCADE)
    session_id = models.CharField(max_length=60)
    login_time = models.DateTimeField()
    logout_time = models.DateTimeField()
    mac_id = models.CharField(max_length=30)
    updated_time = models.TimeField()
    execute_command = models.CharField(max_length=500)
    availability = models.IntegerField()
    host_name = models.CharField(max_length=30)
    kite_version = models.CharField(max_length=500)


class TEC_USER_QUERIES(models.Model):
    id = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    query_response = models.CharField(max_length=1000)
    user_id = models.ForeignKey(TEC_USER, on_delete=models.CASCADE)
    timestamp = models.TimeField(null=True)