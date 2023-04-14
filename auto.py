import re

emails = []
phone_numbers = []

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone_regex = r'(\d{3})[.-]?(\d{3})[.-]?(\d{4})'

with open('assets/potential_contacts.txt', 'r') as file:
    contents = file.read()

emails = re.findall(email_regex, contents)

phone_numbers = re.findall(phone_regex, contents)

for match in re.finditer(phone_regex, contents):
    area_code = match.group(1)
    if area_code != '206' and not match.group(0).startswith('('):
        area_code = '206'
    phone_numbers.append(f'{area_code}-{match.group(2)}-{match.group(3)}')

emails = sorted(list(set(emails)))
for i, phone in enumerate(phone_numbers):
    if isinstance(phone, tuple):
        phone = list(phone)
        phone = '-'.join(list(map(str, phone)))
        phone_numbers[i] = phone
    if isinstance(phone, list):
        phone = str(phone)
        phone_numbers[i] = phone

phone_numbers = sorted(set(phone_numbers))
print(phone_numbers)

with open('emails.txt', 'w') as file:
    file.write('\n'.join(emails))

with open('phone_numbers.txt', 'w') as file:
    for phone_number in phone_numbers:
        file.write(phone_number + '\n')
