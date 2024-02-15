from django.contrib import admin
from newsletter.models import Newsletter, Suscriptor, Template, Category

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
  list_display = ['name','subject', 'content']

@admin.register(Suscriptor)
class SuscriptorAdmin(admin.ModelAdmin):
  list_display = ['email', 'name', 'suscribed']
  filter_horizontal = ('excluded_categories',) 

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
  pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  pass