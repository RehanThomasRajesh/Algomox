# analytics_dashboard/management/commands/fetch_social_media_data.py
from django.core.management.base import BaseCommand
from analytics_dashboard.api import fetch_social_media_data

class Command(BaseCommand):
    help = 'Fetch social media data from APIs'

    def handle(self, *args, **options):
        fetch_social_media_data()
        self.stdout.write(self.style.SUCCESS('Successfully fetched social media data'))
