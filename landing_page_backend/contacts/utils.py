import csv

with open('contacts-2022-09-01.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(
        ('name', 'email', 'number', 'message')
    )


def write_data_to_sfv_file(contact):
    with open('contacts-2022-09-01.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow(
            contact
        )
