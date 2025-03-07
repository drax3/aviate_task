from django.shortcuts import render
from rest_framework import generics
from .models import Candidate
from .serializers import CandidateSerializer
from django.db.models import Count, Q

# Create your views here.
# Create Candidate
class CandidateCreateView(generics.CreateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# List All Candidate
class CandidateListView(generics.ListAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

# Detail View
class CandidateDetailView(generics.RetrieveAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'


# Update Candidate
class CandidateUpdateView(generics.UpdateAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'

# Delete Candidate
class CandidateDeleteView(generics.DestroyAPIView):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    lookup_field = 'id'

# Search Candidate
class CandidateSearchView(generics.ListAPIView):
    serializer_class = CandidateSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')

        if not query:
            return Candidate.objects.none()

        search_words = query.split()

        q_objects = Q()
        for word in search_words:
            q_objects |= Q(name__icontains=word)

        context=Candidate.objects.filter(q_objects).annotate(match_count=Count('name', filter=q_objects)).order_by('-match_count')
        return context