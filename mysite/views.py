from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	myname = "Yuan"
	return render(request, 'index.html', locals())

# Create your views here.
