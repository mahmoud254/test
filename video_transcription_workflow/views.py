from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.views.generic import ListView
from .models import VideoTranscript

# Create your views here.
class HomePageView(TemplateView):
    template_name='index.html'

class VideoTranscriptionWorkflow(TemplateView):
    template_name='video_transcription_workflows/video_transcription_workflow.html'

class InitializationView(ListView):
    template_name='video_transcription_workflows/video_transcription_workflow_initialization.html'
    model=VideoTranscript


class CorrectionView(ListView):
    template_name='video_transcription_workflows/video_transcription_workflow_correction.html'
    model=VideoTranscript

class RevisionView(ListView):
    template_name='video_transcription_workflows/video_transcription_workflow_revision.html'
    model=VideoTranscript

class VideoTranscriptionAddView(CreateView):
    template_name='video_transcription_workflows/video_transcription_add.html'
    model=VideoTranscript
    fields='__all__'
