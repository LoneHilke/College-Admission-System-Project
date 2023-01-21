from django.shortcuts import render
from .models import Application, Notice, Detail

# Create your views here.
def college(request):
    notice = Notice.objects.all()
    return render(request, "college.html", {'notice':notice})


# from: https://data-flair.training/blogs/python-college-admission-system/