from django.shortcuts import render
from .models import Note
from django.contrib.auth.decorators import login_required

@login_required
def note_list(request):
    notes = Note.objects.filter(owner=request.user).order_by('-updated_at')
    return render(request, 'notes/note_list.html', {'notes': notes})
