from django.db import models
import datetime
from django.utils import timezone

class Note(models.Model):
    note_label = models.CharField(max_length=50)
    note_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.note_label

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
