from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from .models import SocialMediaData
from django.views.decorators.cache import cache_page
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

def dashboard(request):
    user_data = SocialMediaData.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'data': user_data})

@cache_page(60 * 15)  # Cache for 15 minutes
def get_chart_data(request):
    start_date = request.GET.get('start_date', None)
    end_date = request.GET.get('end_date', None)
    platform = request.GET.get('platform', None)

    queryset = SocialMediaData.objects.all()

    if start_date and end_date:
        queryset = queryset.filter(date__range=[start_date, end_date])

    if platform:
        queryset = queryset.filter(platform=platform)

    data = queryset.values('date', 'followers', 'engagements', 'impressions')

    # Convert the queryset to a format suitable for Chart.js
    labels = [str(entry['date']) for entry in data]
    followers = [entry['followers'] for entry in data]
    engagements = [entry['engagements'] for entry in data]

    return JsonResponse({
        'labels': labels,
        'datasets': [
            {'label': 'Followers', 'data': followers},
            {'label': 'Engagements', 'data': engagements},
        ],
    })

def login(request):
    form = AuthenticationForm()  # Initialize the form outside of the if block

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                # Redirect to the dashboard or any other desired page
                return redirect('dashboard')

    return render(request, 'login.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
