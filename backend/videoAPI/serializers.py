from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Video
    fields = '__all__'  # Include all fields

  # Alternatively, specify only desired fields
  # fields = ['id', 'title', 'description', 'upload_date']