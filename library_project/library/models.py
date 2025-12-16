from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=128) 
    email = models.EmailField(unique=True) 
    address = models.CharField(
        max_length=256, 
        blank=True, 
        null=True 
    ) 
    
    def __str__(self): 
        return f"{self.name} - {self.email}" 


class Book(models.Model): 
    title = models.CharField(max_length=256) 
    published_date = models.DateField() 
    author = models.ForeignKey(
        Author, 
        on_delete=models.CASCADE, 
        related_name='books_author' 
    ) 
    
    def __str__(self): 
        return f"{self.title} - {self.author.name}"

