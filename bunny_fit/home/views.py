from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    return HttpResponse("<h5>Page was found</h5>")