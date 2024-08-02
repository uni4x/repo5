from django.db import models

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:50]

class Tag(models.Model):
    name = models.CharField(max_length=255)
    notes = models.ManyToManyField(Note, related_name='tags')

    def __str__(self):
        return self.name