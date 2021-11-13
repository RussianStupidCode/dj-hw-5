from rest_framework.serializers import ModelSerializer
from django.forms.fields import ImageField
from measurements.models import Project, Measurement


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementSerializer(ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
