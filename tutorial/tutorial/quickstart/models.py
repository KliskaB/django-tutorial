from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ToDo(models.Model):
    HIGH = 'H'
    MEDIUM = 'M'
    LOW = 'L'
    PRIORITY_CHOICES = [
        (HIGH, 'High'),
        (MEDIUM, 'Medium'),
        (LOW, 'Low'),
    ]

    title = models.CharField(max_length=100)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITY_CHOICES,
        default=LOW,
    )
    user = models.ForeignKey(User, on_delete=models.PROTECT)
 
    def __str__(self):
        return self.title
