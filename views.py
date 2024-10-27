from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.conf import settings
from .forms import ProfileForm
from django.contrib import messages
from .serializers import UserProfileSerializer
from .models import UserProfile
from rest_framework import generics
from urllib.parse import urlencode


class UserProfileViewSet(generics.ListAPIView):
    serializer_class = UserProfileSerializer

    def get_queryset(self):
        user = self.request.user.id
        return UserProfile.objects.filter(user=user)


def index(request):
    return render(request, 'home.html')


def login(request):
    return redirect('/login/auth0')


def logout(request):
    auth_logout(request)
    return_to = urlencode({'returnTo': settings.LOGOUT_REDIRECT_URL, 'client_id': settings.AUTH0_CLIENT_ID})
    return redirect(f'https://{settings.AUTH0_DOMAIN}/v2/logout?{return_to}')


@login_required
def dashboard(request):
    profile = UserProfile.objects(user=request.user).first()
    return render(request, 'dashboard.html', {'profile': profile})


@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = UserProfile(
                user=request.user,
                username=form.cleaned_data['username'],
                age=form.cleaned_data['age'],
                bio=form.cleaned_data['bio'],
                gender=form.cleaned_data['gender'],
                location=form.cleaned_data['location'],
                interests=form.cleaned_data['interests'],
            )
            profile.save()
            messages.success(request, 'Profile created successfully!')
            return redirect('dashboard')
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form})
