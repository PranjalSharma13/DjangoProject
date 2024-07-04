from django.shortcuts import render
from django.http import HttpResponse
from . models import Collection,Piece
# Create your views here.
def index(request):
    all_collection=Collection.objects.all()
    context = {'all_collection':all_collection}
    return HttpResponse("<h1>Hello World</h1>")

def details(request, app_id):
    return HttpResponse("<h1>The genre id is " + str(app_id) + "</h1>")

