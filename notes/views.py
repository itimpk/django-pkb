from django.shortcuts import render , redirect
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import NoteForm

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user).order_by('-updated_at')
    return render(request, 'notes/note_list.html', {'notes': notes})


def note_form(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        form.save_m2m()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})


def note_detail(request, id):
    note = Note.objects.get(id=id, owner=request.user)
    return render(request, 'notes/note_detail.html', {'note': note})

def note_update(request, id):
    note = Note.objects.get(id=id, owner=request.user)
    form = NoteForm(request.POST or None, instance=note)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})