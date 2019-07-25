from django.db import models

# Create your models here.

class disease(models.Model):
    dis_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.dis_name

class excercise(models.Model):
    dis = models.ForeignKey(disease, on_delete=models.CASCADE, related_name='choice_set')
    ex_name = models.CharField(max_length = 50)
    anim = models.FileField(null=True, blank=True)
    def __str__(self):
        return self.ex_name
