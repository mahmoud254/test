from django.db import models
from django.urls import reverse
from django.utils import timezone

class VideoTranscript(models.Model):
    status_choices  = [('Approved','Approved'),('Not Approved','Not Approved'),('In Update Process','In Update Process')]

    transcriptID    = models.IntegerField(primary_key=True)
    creationDate    = models.DateTimeField(default=timezone.now ,editable=False)
    fileFormat      = models.CharField(max_length=10)
    status          = models.CharField(max_length=30, choices = status_choices)

class VideoTranscriptionVersion(models.Model):
    currentRole_choices = [('Initialization','Initialization'),('Correction','Correction'),('Finalization','Finalization')]
    status_choices  = [('Approved','Approved'),('Not Approved','Not Approved'),('In Update Process','In Update Process')]

    versionNumber   = models.IntegerField(primary_key=True)
    transcriptID    = models.ForeignKey(VideoTranscript, on_delete=models.CASCADE)
    currentRole     = models.CharField(max_length=30, choices = currentRole_choices)
    submittionDate  = models.DateTimeField(default=timezone.now,editable=False)
    comment         = models.TextField()
    filePath        = models.TextField()
    status          = models.CharField(max_length=30, choices = status_choices)

