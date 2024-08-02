from django.shortcuts import render, redirect, get_object_or_404
from .models import Note, Tag
from .forms import NoteForm
from django.forms import modelformset_factory
from django.http import JsonResponse
from markdown import markdown
# import bleach


def index(request):
    notes = Note.objects.all()
    for note in notes:
        # コンテンツを最初の1行だけに変更
        first_line = note.content.splitlines()[0] if note.content else ""
        note.first_line = first_line
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)

def create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return redirect('notes:index')
    else:
        form = NoteForm()
    return render(request, 'notes/create.html', {'form': form})

def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)  # まだ保存しない
            note.save()  # Noteモデルを保存

            # 既存のタグをすべて削除
            note.tags.clear()

            # 新しいタグを追加
            tag_names = form.cleaned_data['tags'].split(',')
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)

            return redirect('notes:index')
    else:
        form = NoteForm(instance=note, initial={'tags': ', '.join([tag.name for tag in note.tags.all()])})
    return render(request, 'notes/edit.html', {'form': form, 'note': note})

def delete(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    note.delete()
    return redirect('notes:index')


def preview(request):
    content = request.POST.get('content', '')
    html = markdown(content, extensions=['extra'])
    return JsonResponse({'html': html})

