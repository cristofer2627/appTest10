from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index (request):
    return HttpResponse("············· You are in the index file. ···················")

def hello (request):
    return HttpResponse("············· This is another Message ···················")
    
def ListClients (request):
    return HttpResponse("Here you must list the clients in DB")
