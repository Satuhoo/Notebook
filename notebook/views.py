from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.http import Http404
from .models import Note

def index(request):
    latest_notes = Note.objects.order_by('-pub_date')[:5]
    template = loader.get_template('index.html')
    context = {
        'latest_notes': latest_notes,
    }
    return HttpResponse(template.render(context, request))

def open_note(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'open_note.html', {'note': note})
    