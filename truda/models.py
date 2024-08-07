from django.db import models

# Create your models here.

class Truda_truth(models.Model):
    truth = models.CharField(max_length=200)

    def __str__(self):
        return self.truth
    

class Truda_dare(models.Model):
    dare = models.CharField(max_length=200)

    def __str__(self):
        return self.dare