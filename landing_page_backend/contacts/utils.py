import csv

from contacts.models import Contact

from datetime import date, timedelta

date = date.today()
file_name = f'contacts-{date}.csv'
one_week_ago = date - timedelta(days=7)


def export_contacts_to_csv_file():
    contacts = Contact.objects.filter(create__gte=one_week_ago).values_list('name', 'email', 'number', 'message')

    file = open(f'contacts/reports/{file_name}', 'w', newline='')

    with file:
        header = ['name', 'email', 'number', 'message']

        write = csv.writer(file)
        write.writerow(header)
        for fields in contacts:
            write.writerow(fields)
