from django.shortcuts import render
from http.client import HTTPConnection
from django.http import JsonResponse


def homepage(request):
	return render(request, 'home.html')

def new_client(request):
	return render(request, 'add_client.html')
