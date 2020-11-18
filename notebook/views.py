from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Note

def index(request):
    latest_notes = Note.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_notes': latest_notes,
    }
    return HttpResponse(template.render(context, request))
