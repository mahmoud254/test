from django.urls import path
from .views import HomePageView
from .views import VideoTranscriptionWorkflow
from .views import  InitializationView
from .views import  CorrectionView
from .views import  RevisionView
from .views import  VideoTranscriptionAddView
urlpatterns = [

    path('',HomePageView.as_view(),name='index'),
    path('vtw',VideoTranscriptionWorkflow.as_view(),name='vtw'),
    path('init',InitializationView.as_view(),name='init'),
    path('add_document',VideoTranscriptionAddView.as_view(),name='add_document'),
    path('review',RevisionView.as_view(),name='review'),
    path('correct',CorrectionView.as_view(),name='correct'),

]
