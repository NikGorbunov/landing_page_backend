from django.contrib import admin

from contacts.models import PreviousProjects, OngoingProjects, ContactModel

admin.site.register(PreviousProjects)
admin.site.register(OngoingProjects)
admin.site.register(ContactModel)
