from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.models import Employee

class AddCreateView(CreateView):
    model = Employee
    template_name = 'demoapp/create.html'
    success_url = ''

