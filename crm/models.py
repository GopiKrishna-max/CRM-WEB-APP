from django.db import models
from django.contrib.auth import get_user_model

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    company = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Deal(models.Model):
    STAGES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    ]
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='deals')
    title = models.CharField(max_length=200)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    stage = models.CharField(max_length=20, choices=STAGES, default='new')
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
