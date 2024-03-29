from django.db import models
from django.utils import timezone

class Category(models.Model):
  topic = models.CharField(max_length=255, unique=True)

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
  attached_file = models.FileField(upload_to='attached_files/', blank=True, null=True)

  def __str__(self):
    return self.name

class Newsletter(models.Model):
  name = models.CharField(max_length=100)
  template = models.ForeignKey(Template, on_delete=models.PROTECT)
  date_sent = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  count_sent = models.IntegerField(default=0)

  def __str__(self):
    return self.name