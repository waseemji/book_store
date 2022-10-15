from email.policy import default
from unittest.util import _MAX_LENGTH
from wsgiref.validate import validator
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.utils.text import slugify
from django.urls import reverse




# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(5)]
        )
    author = models.CharField(null=True,max_length=100)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",blank=True,null=False,db_index=True)

    def get_absolute_url(self):
        return reverse("book-details", args=[self.slug])
    

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.title} ({self.rating}) Author:{self.author} \t Best Selling: {self.is_bestselling} "