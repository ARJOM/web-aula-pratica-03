from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['name', 'registration', 'email', 'cpf', 'date_birth']