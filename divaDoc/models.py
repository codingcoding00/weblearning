from django.db import models

# Create your models here.

class Testdoc(models.Model):
    d_type = models.CharField(max_length = 25)
    def __str__(self):
        return self.d_type

class TestChoice(models.Model):
    doc = models.ForeignKey(Testdoc, on_delete=models.CASCADE, related_name='choice_set')
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    available_dates = models.CharField(max_length = 200)
    works_from = models.IntegerField()
    works_upto = models.IntegerField()
    init_date = models.IntegerField(default = 1)
    curr_status = models.IntegerField(default = 0)
    max_booking = models.IntegerField(default = 70)
    def __str__(self):
        return self.name


    
##################### RATING
    
class rateapp(models.Model):
    rating = models.IntegerField(default=0)


"""
class disease(models.Model):
    dis_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.dis_name

class medicine(models.Model):
    dis = models.ForeignKey(disease, on_delete=models.CASCADE, related_name='choice_set')
    med_name = models.CharField(max_length = 50)
    def __str__(self):
        return self.med_name
"""
