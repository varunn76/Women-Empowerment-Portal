from django.db import models


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    password = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.name
