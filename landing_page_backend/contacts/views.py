from rest_framework.generics import CreateAPIView
import csv
from contacts.models import Contact
from contacts.serializers import ContactSerializer

with open('data.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('name', 'email', 'number', 'message')
    )


class ContactAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    contacts = Contact.objects.all().values_list('name', 'email', 'number', 'message')
    for contact in contacts:
        with open('data.csv', 'a') as file:
            writer = csv.writer(file)
            writer.writerow(
                contact
            )
