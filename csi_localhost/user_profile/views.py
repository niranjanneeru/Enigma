from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.utils.timezone import now
from django.views import View

from csi_localhost.rules.models import Rules
from .forms import ProfileForm, ProfileDetailForm
from .models import Profile


class ProfileView(View):
    def get(self, request):
        user = request.user
        try:
            profile = user.profile
            return render(request, 'profile/start.html', {'rules': Rules.objects.all().order_by('priority')})
        except Profile.DoesNotExist:
            form = ProfileForm(initial={'nick_name': user.username})
            return render(request, 'profile/profile.html', {'form': form})

    def post(self, request):
        form = ProfileForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.last_submission = now()
            form.save()
            return render(request, 'profile/start.html', {'rules': Rules.objects.all().order_by('priority')})


class ProfileChangeView(View):
    def get(self, request):
        user = request.user
        form = ProfileDetailForm()
        return render(request, 'profile/profile.html', {'form': form})

    def post(self, request):
        form = ProfileDetailForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            profile = request.user.profile
            if name:
                profile.name = name
                profile.save()
            return render(request, 'profile/start.html', {'rules': Rules.objects.all().order_by('priority')})


def leader_view(request):
    profiles = Profile.objects.filter(marks__gt=0)
    context = {'profiles': profiles.order_by('-marks', 'last_submission')}

    if request.user.is_authenticated:
        try:
            profile = request.user.profile
            if profile:
                if profile.current_question:
                    context['text'] = "Let's Continue"
                    context['has_started'] = True
                else:
                    context['text'] = "Let's Start"
                    context['has_started'] = False
        except Profile.DoesNotExist:
            context['text'] = "Let's Start"
            context['has_started'] = False
    else:
        context['text'] = "Let's Start"
        context['has_started'] = False
    return render(request, 'profile/lead.html', context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
