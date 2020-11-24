from django.http import HttpResponse
from django.shortcuts import render
from django.http import Http404
from .models import Note
from django.utils import timezone

def index(request):
    latest_notes = Note.objects.order_by('-pub_date')
    context = {
        'latest_notes': latest_notes,
    }
    return render(request, 'index.html', context)

def open_note(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404("Note does not exist")
    return render(request, 'open_note.html', {'note': note})

def create_note(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        text = request.POST.get('text')
        note = Note(note_label = label, note_text = text, pub_date = timezone.now())
        note.save()
        
        return HttpResponse("Saved succesfully!")

    