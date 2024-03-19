from rest_framework import serializers
from .models import projects

class projects_serializers(serializers.ModelSerializer):
    class Meta:
        model = projects 
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)

