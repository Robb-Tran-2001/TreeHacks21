from django.shortcuts import render
from django.http import HttpResponse
# Create your endpoints here.

def main(request):
    print(request)
    return HttpResponse("<h1>Hello</h1>")