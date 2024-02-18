"""
URL configuration for codecraft_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from newsletter.api.views import SuscriptorApiView
from newsletter.api.views import TemplateDetailView
from newsletter.api.views import TemplateListView
from newsletter.api.views import CategoryListView
from newsletter.api.views import CategoryUpdateDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/suscriptors/', SuscriptorApiView.as_view()),
    path('api/templates/', TemplateListView.as_view()),
    path('api/templates/<int:pk>/', TemplateDetailView.as_view()),
    path('api/categories/', CategoryListView.as_view()),
    path('api/categories/<int:pk>/', CategoryUpdateDeleteView.as_view())
] + static(settings.ATTACHED_FILES_URL, document_root=settings.ATTACHED_FILES_ROOT)