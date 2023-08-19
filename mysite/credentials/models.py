from django.db import models

class Branch(models.Model):
    district = models.CharField(max_length=100)
    wikipedia_link = models.URLField()

    def __str__(self):
        return self.district

class Application(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.TextField(max_length=250)
    district = models.CharField(max_length=50)
    branch = models.CharField(max_length=50)
    account_type = models.CharField(max_length=50)
    materials = models.CharField(max_length=50)

    def __str__(self):
        return self.name