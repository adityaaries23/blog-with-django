import bson
from django.shortcuts import render

def generate_id():
    return str(bson.ObjectId())


def custom_404(request):
    return render(request, 'error/404.html', status=404)