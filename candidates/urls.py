from tkinter.font import names

from django.urls import path
from .views import CandidateCreateView, CandidateListView, CandidateDetailView, CandidateUpdateView, CandidateDeleteView, CandidateSearchView

urlpatterns = [
    path('', CandidateListView.as_view(), name='candidate-listall'),
    path('<int:id>/', CandidateDetailView.as_view(), name='candidate-detail'),
    path('create/', CandidateCreateView.as_view(), name='candidate-create'),
    path('update/<int:id>/', CandidateUpdateView.as_view(), name='candidate-update'),
    path('delete/<int:id>/', CandidateDeleteView.as_view(), name='candidate-delete'),
    path('search/', CandidateSearchView.as_view(), name='candidate-search'),
]
