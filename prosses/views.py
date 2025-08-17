# views.py
from rest_framework import viewsets
from .models import ProcessStep
from .serializers import ProcessStepSerializer

class ProcessStepViewSet(viewsets.ModelViewSet):
    queryset = ProcessStep.objects.all()
    serializer_class = ProcessStepSerializer
