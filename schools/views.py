from .models import School
from rest_framework import serializers, viewsets

# Serializers define the API representation.
class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['name', 'address']

# ViewSets define the view behavior.
class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer