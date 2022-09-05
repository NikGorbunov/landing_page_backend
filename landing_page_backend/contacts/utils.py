import csv

from contacts.models import Contact

from datetime import date, timedelta

date = date.today()
file_name = f'contacts-{date}.csv'
one_week_ago = date - timedelta(days=7)

with open(f'contacts/reports/{file_name}', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('name', 'email', 'number', 'message')
    )


def write_data_to_csv_file():
    contacts = Contact.objects.filter(time_create__gte=one_week_ago).values_list('name', 'email', 'number', 'message')

    for contact in contacts:
        file = open(f'contacts/reports/{file_name}', 'a')
        with file:
            writer = csv.writer(file)
            writer.writerow(
                contact
            )
