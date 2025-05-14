from django.shortcuts import render , redirect , get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required
from .forms import NoteForm
from .filters import NoteFilter
from django.contrib import messages
from django.db.models import Q

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user)
    note_filter = NoteFilter(request.GET, queryset=notes)
    return render(request, 'notes/note_list.html', {
        'filter': note_filter,
        'notes': note_filter.qs,
    })


def note_form(request):
    form = NoteForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        note = form.save(commit=False)
        note.owner = request.user
        note.save()
        form.save_m2m()
        messages.success(request, "Note Created!")
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
        messages.info(request, "Note Updated!")
        return redirect('note_list')
    return render(request, 'notes/note_form.html', {'form': form})

def note_delete(request, id):
    note = Note.objects.get(id=id, owner=request.user)
    if request.method == 'POST':
        note.delete()
        messages.error(request, "Note Deleted!")
        return redirect('note_list')
    return redirect('note_detail', id=id)