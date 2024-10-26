from django.shortcuts import render
from django.shortcuts import redirect
from urllib.parse import urlencode
from django.conf import settings
import json
import requests
from django.http import HttpResponseRedirect
from .models import Profile
from django.http import HttpResponse

def profile(request):
    user = request.session.get('user', None)
    if not user:
        return redirect('/login/')  # Redirect to login if user not logged in
    
    if request.method == 'POST':
        # Profile form submitted
        name = request.POST.get('name')
        bio = request.POST.get('bio')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        
        # Save profile to MongoDB
        profile = Profile.objects.create(
            user_id=user['user_id'],
            name=name,
            email=user['email'],
            bio=bio,
            age=age,
            gender=gender,
            location=location
        )
        profile.save()

        return HttpResponse("Profile created successfully!")
    
    return render(request, 'profile.html')


def login(request):
    """Redirects to the Auth0 login page."""
    return HttpResponseRedirect(f"https://{settings.AUTH0_DOMAIN}/authorize?" + urlencode({
        "response_type": "code",
        "client_id": settings.AUTH0_CLIENT_ID,
        "redirect_uri": settings.AUTH0_CALLBACK_URL,
        "scope": "openid profile email",
    }))

def callback(request):
    """Handles callback from Auth0 after login."""
    code = request.GET.get('code')
    token_url = f"https://{settings.AUTH0_DOMAIN}/oauth/token"
    
    token_payload = {
        "grant_type": "authorization_code",
        "client_id": settings.AUTH0_CLIENT_ID,
        "client_secret": settings.AUTH0_CLIENT_SECRET,
        "code": code,
        "redirect_uri": settings.AUTH0_CALLBACK_URL,
    }
    
    token_info = requests.post(token_url, json=token_payload).json()
    user_info_url = f"https://{settings.AUTH0_DOMAIN}/userinfo"
    headers = {"Authorization": f"Bearer {token_info['access_token']}"}
    
    user_info = requests.get(user_info_url, headers=headers).json()
    
    # Now that you have user information, store it in the session or database
    request.session['user'] = {
        'user_id': user_info['sub'],
        'name': user_info['name'],
        'email': user_info['email'],
    }
    
    return redirect('/profile/')

