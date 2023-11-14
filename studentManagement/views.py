from django.shortcuts import render

from studentManagement.models import Student


def list_view(request):
    items = Student.objects.all()
    return render(request, 'list.html', {'items': items})
