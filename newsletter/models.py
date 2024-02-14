from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Suscriptor(models.Model):
  email = models.EmailField(primary_key=True)
  name = models.CharField(max_length=100)
  suscribed = models.BooleanField(default=True)
  def __str__(self):
    return self.email

class Template(models.Model):
  name = models.CharField(default="")
  subject = models.CharField(max_length=200)
  content = models.TextField()

  def __str__(self):
    return self.name
class Newsletter(models.Model):
  name = models.CharField(max_length=100)
  sending_date = models.DateTimeField()
  template = models.ForeignKey(Template, on_delete=models.PROTECT)
  def __str__(self):
    return self.name

  def clean(self):
    super().clean()
    if self.sending_date < timezone.now():
      raise ValidationError("Sending date needs to be equal or later than now")

class Sent_Logs(models.Model):
  date_sent = models.DateTimeField(auto_now_add=True)
  suscriptor = models.ForeignKey(Suscriptor, on_delete=models.PROTECT)
  newsletter = models.ForeignKey(Newsletter, on_delete=models.PROTECT)