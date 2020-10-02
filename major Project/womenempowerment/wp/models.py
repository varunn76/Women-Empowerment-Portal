from django.db import models


class Feedback(models.Model):
    msg_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, default="")
    Phone_no = models.CharField(max_length=10)
    message = models.CharField(max_length=500, default="")

    # def __str__(self):
    #     return self.first_name