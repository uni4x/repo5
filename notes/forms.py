from django import forms
from .models import Note, Tag


class NoteForm(forms.ModelForm):
    tags = forms.CharField(required=False)

    class Meta:
        model = Note
        fields = ['title', 'content'] 

    def save(self, commit=True):
        note = super().save(commit=False)
        if commit:
            note.save()
        # タグの保存
        if 'tags' in self.cleaned_data:
            tag_names = self.cleaned_data['tags'].split(',')
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name.strip())
                note.tags.add(tag)
        return note