from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context_dict = { 'boldmessage': "yo bold" }
	return render(request, 'rango/index.html', context_dict)
