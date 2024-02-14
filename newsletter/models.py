from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Suscriptor(models.Model):
  email = models.EmailField(primary_key=True)
  name = models.CharField(max_length=100)
  suscribed = models.BooleanField()

class Template(models.Model):
  subject = models.CharField(max_length=200)
  content = models.CharField()

class Audience(models.Model):
  name = models.CharField(max_length=100)
  suscriptor = models.ManyToManyField(Suscriptor)

class Newsletter(models.Model):
  name = models.CharField(max_length=100)
  sending_date = models.DateField()
  audience = models.ManyToManyField(Audience)
  template = models.ForeignKey(Template, on_delete=models.PROTECT)

  def clean(self):
    super().clean()
    if self.sending_date < timezone.now().date():
      raise ValidationError("Sending date needs to be equal or later than now")

class Sent_Logs(models.Model):
  date_sent = models.DateTimeField(auto_now_add=True)
  suscriptor = models.ForeignKey(Suscriptor, on_delete=models.PROTECT)
  newsletter = models.ForeignKey(Newsletter, on_delete=models.PROTECT)