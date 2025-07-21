from django.shortcuts import render
from .models import Project
from .forms import ContactForm


def home(request):
    """Creates the homepage."""
    projects = Project.objects.all()
    return render(request, "home.html",
                  {"projects": projects})


def project_list(request):
    """Creates the project list."""
    projects = Project.objects.all()
    return render(request, "project_list.html",
                  {"projects": projects})


def project(request, pk):
    """Creates project page."""
    project = Project.objects.filter(pk=pk).first()
    return render(request, "project.html",
                  {"project": project})


def contact_page(request):
    """Creates the contact page."""
    success = False
    if (request.method == "POST"):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            success = True
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, "contact_page.html",
                  {"form": form, "success": success})


def base_template(request):
    """Creates the base template."""
    return render(request, "base_template.html")
