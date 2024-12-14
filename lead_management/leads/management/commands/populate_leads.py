from django.core.management.base import BaseCommand
from leads.models import Lead
from faker import Faker

class Command(BaseCommand):
    help = 'Populate database with leads'

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100):
            # Ensure the phone number length does not exceed 15 characters
            phone = fake.phone_number()
            if len(phone) > 15:
                phone = phone[:15]  # Truncate if necessary

            Lead.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),  # Ensure unique emails
                phone=phone,
            )

        self.stdout.write(self.style.SUCCESS('Successfully added 100 fake leads'))
