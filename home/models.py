from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=13)
    textarea = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Massage form {self.name}"