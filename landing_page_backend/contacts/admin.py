from django.contrib import admin

from contacts.models import Contact, Project

admin.site.register(Project)
admin.site.register(Contact)
