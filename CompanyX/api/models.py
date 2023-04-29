from django.db import models

# Create your models here.
class Company(models.Model):
    Company_id = models.AutoField(primary_key=True)
    name = models.models.CharField(max_length=50)
    location = models.CharField(max_length=25)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ('Non IT','Non IT')))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    

