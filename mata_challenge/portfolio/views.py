from django.shortcuts import render

def base_template(request):
    """Creates the base template."""
    return render(request, "base_template.html")
