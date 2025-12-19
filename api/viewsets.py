from rest_framework import viewsets
from .models import *
from .serializers import *

class TVViewSet(viewsets.ModelViewSet):
    queryset = TV.objects.all()
    serializer_class = TVSerializer