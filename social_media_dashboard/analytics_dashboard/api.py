# analytics_dashboard/api.py
from .models import SocialMediaData
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()

def fetch_social_media_data():
    # Implement API calls to fetch data from social media platforms
    # Example: Fetch data from Facebook Graph API
    facebook_token = os.getenv('FACEBOOK_ACCESS_TOKEN')
    facebook_response = requests.get(f'https://graph.facebook.com/v12.0/me?fields=followers_count,engagement,impressions&access_token={facebook_token}')
    facebook_data = json.loads(facebook_response.text)
    
    # Extract 'date' with a default value or handle if it's missing
    date_data = facebook_data.get('date', None)

    # Save data to the database
    SocialMediaData.objects.create(
        platform='Facebook',
        date=date_data,
        followers=facebook_data.get('followers_count', 0),
        engagements=facebook_data.get('engagement', 0),
        impressions=facebook_data.get('impressions', 0)
    )
    # Repeat similar steps for other social media platforms

# Call the fetch_social_media_data function to fetch and save data
fetch_social_media_data()
