from django.db import models

# to only allow mp4 videos used in model Video
from django.core.validators import FileExtensionValidator

def video_upload_to(instance, filename):
  # This function defines the upload path for videos
  ext = filename.split('.')[-1]
  return f'videos/{instance.title}.{ext}'  # Customize path format if needed

class Video(models.Model):
  title = models.CharField(max_length=255)
  description = models.TextField(blank=True)

  file = models.FileField(upload_to=video_upload_to, validators=[FileExtensionValidator(allowed_extensions=['mp4'])])
  upload_date = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title
