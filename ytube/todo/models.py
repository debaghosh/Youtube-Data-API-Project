from django.db import models

class List(models.Model):
    title = models.CharField(max_length=200)
    link = models.CharField(max_length=1000,default=False)
    #complete = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

