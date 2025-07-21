from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import base_template, home, project_list, contact_page, project

urlpatterns = [
    path("", home, name="home"),
    path("projects/", project_list, name="project-list"),
    path("project/<int:pk>", project, name="project"),
    path("contact/", contact_page, name="contact"),
    path("base", base_template, name="base"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)