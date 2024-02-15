from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Category(models.Model):
  topic = models.CharField(max_length=255)

  def __str__(self):
    return self.topic

class Suscriptor(models.Model):
  email = models.EmailField(primary_key=True)
  name = models.CharField(max_length=100)
  suscribed = models.BooleanField(default=True)
  excluded_categories = models.ManyToManyField(Category)

  def __str__(self):
    return self.email

class Template(models.Model):
  name = models.CharField(default="")
  subject = models.CharField(max_length=200)
  content = models.TextField()
  category_id = models.ForeignKey(Category, on_delete=models.PROTECT)

  def __str__(self):
    return self.name
class Newsletter(models.Model):
  name = models.CharField(max_length=100)
  template = models.ForeignKey(Template, on_delete=models.PROTECT)
  def __str__(self):
    return self.name

class Sent_Logs(models.Model):
  date_sent = models.DateTimeField(auto_now_add=True)
  suscriptor = models.ForeignKey(Suscriptor, on_delete=models.PROTECT)
  newsletter = models.ForeignKey(Newsletter, on_delete=models.PROTECT)