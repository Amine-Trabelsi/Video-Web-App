from .models import Video
from .serializers import VideoSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404

class VideoList(generics.ListAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

class VideoDetail(generics.RetrieveAPIView):
  queryset = Video.objects.all()
  serializer_class = VideoSerializer

  def get_object(self):
    # Override get_object to retrieve video based on specific parameter (e.g., ID)
    lookup_field = self.lookup_field  # Usually 'pk' for primary key
    obj_id = self.kwargs[lookup_field]
    queryset = self.get_queryset()  # Use the base queryset
    queryset = queryset.filter(**{lookup_field: obj_id})  # Filter by ID or other field
    obj = get_object_or_404(queryset)  # Raise 404 if object not found
    return obj