from django.shortcuts import render, redirect
from django.views import View
from .forms import StudentForm
from .models import Student

class StudentListRequestHandler(View):
    def get(self, request):
        return render(request, 'list.html', {'students': Student.objects.all()})

class StudentCreateRequestHandler(View):
    def get(self, request):
        return render(request, 'form.html', {'form' : StudentForm})
    
    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        else:
            return render(request, 'form.html', {'form' : form})