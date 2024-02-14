from django.contrib import admin
from newsletter.models import Newsletter, Suscriptor, Template

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
  list_display = ['name','subject', 'content']

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
  list_display = ['email', 'name', 'suscribed']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
  # list_display = []
  pass