from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand

from contacts.models import Contact
from contacts.utils import write_data_to_sfv_file
from landing_page_backend.settings import EMAIL_HOST_USER


class Command(BaseCommand):
    help = 'Weekly reports'

    def handle(self, *args, **options):
        contacts = Contact.objects.all().values_list('name', 'email', 'number', 'message')
        for contact in contacts:
            write_data_to_sfv_file(contact)

        message = 'Weekly reports'
        subject = 'This is weekly reports'
        email = EmailMessage(subject, message, EMAIL_HOST_USER, ['gorbunovmy.a@gmail.com'])
        file = open('contacts-2022-09-01.csv', 'r')
        email.attach('contacts-2022-09-01.csv', file.read())
        email.send()
