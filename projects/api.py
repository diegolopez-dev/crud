from .models import projects
from rest_framework import viewsets, permissions
from .serializers import projects_serializers

class ProjectViewsets(viewsets.ModelViewSet):
    queryset = projects.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = projects_serializers
