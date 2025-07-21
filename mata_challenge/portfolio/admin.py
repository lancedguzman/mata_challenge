from django.contrib import admin
from django.contrib.auth.models import User
from .models import Project, Profile, Contact


class ProjectAdmin(admin.ModelAdmin):
    """Creates the Project Admin Panel."""
    model = Project
    list_display = ["name", "creator",
                    "description", "status",
                    "first_created",]
    

class ContactAdmin(admin.ModelAdmin):
    """Creates the Contact Admin Panel."""
    model = Contact
    list_display = ["subject", "email",
                    "message", "sent_at",]


class ProfileInline(admin.StackedInline):
    """Creates the Profile Admin Panel."""
    model = Profile
    can_delete = False
    fields = ["name",]


class UserAdmin(admin.ModelAdmin):
    """Sets how Profiles are displayed in Admin Panel."""
    inlines = [ProfileInline]


admin.site.register(Project, ProjectAdmin)

admin.site.register(Contact, ContactAdmin)

admin.site.unregister(User)

admin.site.register(User,UserAdmin)
