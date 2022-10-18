from django.db import models


class Familiar(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    kin = models.CharField(max_length=40)
    email = models.EmailField()
    birth_day = models.DateTimeField(max_length=40)

    def __str__(self):
        return f"{self.name} {self.last_name} |{self.kin} | {self.email} | {self.birth_day}"
# Create your models here.
