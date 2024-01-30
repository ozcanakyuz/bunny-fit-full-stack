from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from home.models import UserProfile, UserProfileForm
from user.forms import UserUpdateForm, ProfileUpdateForm


@login_required(login_url='/login') # Check login
def index(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        password_form = PasswordChangeForm(request.user, request.POST)
        if 'update_submit' in request.POST:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('user_profile')
        elif 'password_submit' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect('/user')
            else:
                messages.error(request, 'Please correct the error below.<br>'+ str(password_form.errors))
                return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        password_form = PasswordChangeForm(request.user)
        context = {'profile': profile,
                   'user_form': user_form,
                   'profile_form': profile_form,
                   'password_form': password_form,
                   'page': 'USER PROFILE',}
        return render(request, 'user_profile.html', context)