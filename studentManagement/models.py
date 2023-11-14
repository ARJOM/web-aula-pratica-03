from django.db import models

# Create your models here.
class Student(models.Model):
    """
    Classe responsável pelo cadastro de alunos
    """
    name = models.CharField(max_length=50, blank=False)
    registration = models.CharField(max_length=10, blank=False)
    email = models.EmailField(max_length=50, blank=False)
    cpf = models.CharField(max_length=11, blank=False)
    date_birth = models.DateField(blank=False)
