from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    """Creates the Project Model."""
    STATUS_CHOICES = [
        ("NS", "Not Started"),
        ("ON", "On Going"),
        ("C", "Completed"),
    ]
    name = models.CharField(max_length=255, default="",
                            blank=True,)
    creator = models.CharField(max_length=255, default="",
                            blank=True,)
    description = models.TextField(max_length=255, default="",
                                   blank=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICES,
                                default="NS")
    image = models.ImageField(upload_to='projects/', blank=True,
                              null=True)
    first_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    

class Contact(models.Model):
    """Creates the Contact Model."""
    subject = models.CharField(max_length=255, default="",
                            blank=True,)
    email = models.EmailField(max_length=255, default="",
                              blank=True)
    message = models.TextField(max_length=255, default="",
                                   blank=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.subject}"


class Profile(models.Model):
    """Creates the Profile Model."""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="")
