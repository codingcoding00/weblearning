from django.db import models

# Create your models here.

class disease(models.Model):
    dis_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.dis_name

class medicine(models.Model):
    dis = models.ForeignKey(disease, on_delete=models.CASCADE, related_name='choice_set')
    med_name = models.CharField(max_length = 50)
    generic_name = models.CharField(max_length = 100, default='')
    drug_class = models.CharField(max_length = 100, default='')
    other = models.CharField(max_length = 5000, default='')
    def __str__(self):
        return self.med_name
