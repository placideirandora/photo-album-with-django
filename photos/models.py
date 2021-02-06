from django.db import models
from uuid import uuid4

# Create your models here.


class Category(models.Model):
    id = models.CharField(
        max_length=225,
        unique=True,
        blank=False,
        null=False,
        default=uuid4,
        primary_key=True)
    name = models.CharField(max_length=100, null=False,
                            blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Photo(models.Model):
    id = models.CharField(
        max_length=225,
        unique=True,
        blank=False,
        null=False,
        default=uuid4,
        primary_key=True)
    name = models.CharField(max_length=100, null=False,
                            blank=False)
    image = models.ImageField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description
