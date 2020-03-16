from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib import messages

@login_required
def profile(request):
    current_user = request.user
    user = User.objects.get(pk=current_user.id)
    
    Profile = apps.get_model('app_registration', 'Profile')
    profile = Profile.objects.filter(user=user).get()
    # print(profile)
    
    if user is not None:
        context = {
            'profile': profile
        }
        return render(request, 'profile.html', context=context)
    else:
        info = messages.info(request, "Something went wrong")
        error = messages.error(request, "Please verify your email_id or username and password correctly!")
        return redirect(request, 'login', {
            'errors': error,
            'messages': info
        })   
    
