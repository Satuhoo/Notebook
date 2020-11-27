from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import Http404
from .models import Note
from django.utils import timezone
from .forms import NoteForm


def index(request):
    latest_notes = Note.objects.order_by('pub_date')
    context = {'latest_notes': latest_notes,}
    
    return render(request, 'index.html', context)

def create_note(request):
    if request.method == 'POST':
        label = request.POST.get('label')
        text = request.POST.get('text')
        note = Note(note_label = label, note_text = text, pub_date = timezone.now())
        note.save()
        
        return redirect('index')
        
def edit(request, note_id):
    if request.method == 'POST':
        note = Note.objects.get(pk=note_id)
        form = NoteForm(request.POST, instance=note)
        form.save()
        
        return redirect('index')

    else:
        note = Note.objects.get(pk=note_id)
        return render(request, 'edit.html', {'note': note})

def delete(request, note_id):
    note = Note.objects.get(pk=note_id)
    note.delete()
    return redirect('index')